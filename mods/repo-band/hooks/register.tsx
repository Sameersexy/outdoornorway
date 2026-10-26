import { atom, read, update } from 'claude-code'
import type { EngineInterface, Register } from 'claude-code'

import type { Repo, Turn } from '../types'

const turn = atom({ plugin: 'repo-band', key: 'turn' } as const, null)
const repo = atom({ plugin: 'repo-band', key: 'repo' } as const, null)
const validator = atom({ plugin: 'repo-band', key: 'validator' } as const, null)
const isHidden = atom({ plugin: 'repo-band', key: 'isHidden' } as const, false)

const git = async ($: EngineInterface, ...args: string[]) => {
  const { exitCode, stdout } = await $.process.run(['git', ...args])

  return exitCode === 0 ? stdout.trim() : ''
}

const refreshRepo = async ($: EngineInterface) => {
  try {
    const branch = (await git($, 'branch', '--show-current')) || 'detached'
    const changed = (await git($, 'status', '--porcelain')).split('\n').filter(Boolean).length
    const next: Repo = { branch, changed }
    await update($, repo, () => next)
  } catch {
    // shortcut: no git here means no repo segment, not an error
  }
}

export const register: Register = on => {
  let startedAt = 0
  let tools = 0

  on('session.start', async ($, e, next) => {
    await refreshRepo($)

    return next(e)
  })

  on('prompt.submit', async ($, e, next) => {
    startedAt = await $.clock.now()
    tools = 0

    return next(e)
  })

  on('tool.call', ($, e, next) => {
    tools += 1

    return next(e)
  })

  on('tool.call', { tool: 'Bash' }, async ($, e, next) => {
    const ran = await next(e)

    if (e.command.includes('script_check.py')) {
      const line = ran.text?.match(/^RESULT: .+$/gm)?.pop()

      if (line) {
        await update($, validator, () => line.slice('RESULT: '.length))
      }
    }

    return ran
  })

  on('turn.complete', async ($, e, next) => {
    const seconds = Math.round(((await $.clock.now()) - startedAt) / 1000)
    const last: Turn = { seconds, tools }
    await refreshRepo($)
    await update($, turn, () => last)

    return next(e)
  })

  on('ui.render', { component: 'AbovePrompt' }, async ($, e, next) => {
    if (e.props.hasSurvey) {
      return next(e)
    }

    const { Box, Button, Text } = $.ui.resolve(e)

    if (await read($, isHidden)) {
      return (
        <Box>
          <Button key="show" label="Show band" plain dimColor onPress={() => update($, isHidden, () => false)} />
        </Box>
      )
    }

    const { cost, context } = await $.session.usage()
    const last = await read($, turn)
    const where = await read($, repo)
    const result = await read($, validator)

    const parts = [
      cost ? `$${cost.usd.toFixed(2)}` : null,
      context.percent === undefined ? null : `context ${context.percent}%`,
      last ? `last turn ${last.seconds}s, ${last.tools} tools` : null,
      where ? `${where.branch}, ${where.changed} changed` : null,
      result ? `check ${result}` : null,
    ].filter(Boolean)

    const compact = async () => {
      try {
        await $.session.compact()
      } catch {
        $.ui.toast('Compact is not available while a turn runs')
      }
    }

    return (
      <Box>
        <Text dimColor>{parts.join(' | ')} </Text>
        {e.props.isWorking ? null : <Button key="compact" label="Compact" onPress={compact} />}
        <Text> </Text>
        <Button key="hide" label="Hide" onPress={() => update($, isHidden, () => true)} />
      </Box>
    )
  })
}

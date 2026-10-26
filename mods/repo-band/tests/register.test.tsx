import { expect, test } from 'claude-code/testing'

const BAND = {
  plugin: 'repo-band',
  component: 'AbovePrompt',
  props: {
    hasSurvey: false,
    isWorking: false,
    maxRows: 10,
    bodyColumns: 80,
    scroll: { offset: 0, bodyRows: 10 },
    view: {},
  },
} as const

const USAGE = {
  startedAt: 0,
  context: { window: 200000, tokens: 62000, percent: 31 },
  rateLimits: [],
  cost: { usd: 0.42 },
}

test('the band shows cost, context, repo and the last check, then hides', async ($, on) => {
  on('session.usage', () => ({ value: USAGE }))
  on('session.start', (_, e) => ({ cwd: e.cwd }))
  on('process.run', (_, e) => ({
    value: {
      exitCode: 0,
      stdout: e.argv.includes('--show-current') ? 'main\n' : ' M a.txt\n?? b.txt\n',
      stderr: '',
      isStdoutTruncated: false,
      isStderrTruncated: false,
    },
  }))
  on('tool.call', (_, e) => ({
    result: {},
    text: e.tool === 'Bash' ? 'x\nRESULT: PASS' : '',
  }))

  await $.session.start({ cwd: '/', surface: 'desktop', isInteractive: true })
  await $.tool.call({ tool: 'Bash', command: 'python3 script_check.py f.md' })

  for (const surface of ['terminal', 'desktop'] as const) {
    const ui = await $.ui.mount({ ...BAND, surface })
    const line = await ui.find({ type: 'Text', text: /\$0\.42/ })

    expect(line?.text).toContain('context 31%')
    expect(line?.text).toContain('main, 2 changed')
    expect(line?.text).toContain('check PASS')
    expect(await ui.find({ key: 'compact' })).toBeDefined()

    await ui.press({ key: 'hide' })
    expect(await ui.find({ key: 'show' })).toBeDefined()
    await ui.press({ key: 'show' })
    await ui.unmount()
  }
})

test('Compact is not offered while a turn runs', async ($, on) => {
  on('session.usage', () => ({ value: USAGE }))

  const ui = await $.ui.mount({
    ...BAND,
    surface: 'desktop',
    props: { ...BAND.props, isWorking: true },
  })

  expect(await ui.find({ key: 'compact' })).toBeUndefined()
  expect(await ui.find({ key: 'hide' })).toBeDefined()
  await ui.unmount()
})

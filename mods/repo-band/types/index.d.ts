export type Turn = { seconds: number; tools: number }
export type Repo = { branch: string; changed: number }

declare module 'claude-code' {
  interface PluginState {
    'repo-band': {
      turn: Turn | null
      repo: Repo | null
      validator: string | null
      isHidden: boolean
    }
  }
}

import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import { resolve } from 'path'

export default defineConfig({
  plugins: [react()],
  build: {
    outDir: '../app/static',
    assetsDir: 'assets',
    manifest: true,
  },
  resolve: {
    alias: {
      '~': resolve(__dirname, 'src'),
      path: 'path-browserify',
      buffer: 'buffer',
    },
  },
})

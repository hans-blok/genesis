-- GitHub Copilot Configuration
-- Disable default Tab mapping for Copilot
vim.g.copilot_no_tab_map = true
vim.g.copilot_assume_mapped = true

-- Optional: Custom keybindings for Copilot
-- Uncomment and adjust as needed:
-- vim.keymap.set('i', '<C-J>', 'copilot#Accept("\\<CR>")', { expr = true, silent = true })
-- vim.keymap.set('i', '<C-]>', '<Plug>(copilot-next)', {})
-- vim.keymap.set('i', '<C-[>', '<Plug>(copilot-previous)', {})
-- vim.keymap.set('i', '<C-\\>', '<Plug>(copilot-dismiss)', {})

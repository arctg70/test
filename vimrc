" 让配置变更立即生效 
"autocmd BufWritePost $MYVIMRC source $MYVIMRC
set nu
set encoding=utf-8
set tabstop=4
set softtabstop=4
set shiftwidth=4
set autoindent
set expandtab 
set fileformat=unix
set showtabline=2
let  mapleader = ","  "设置引导符

"语法高亮
let python_highlight_all=1 
syntax on

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
"set rtp+=~/.vim/bundle/powerline/powerline/bindings/vim
set nocompatible              " required
filetype off                  " required

""""""""""""""""""""""""""""""""""""
" 插件管理
call vundle#begin()
" alternatively, pass a path where Vundle should install plugins
"call vundle#begin('~/some/path/here')

" let Vundle manage Vundle, required
Plugin 'gmarik/Vundle.vim'

" Add all your plugins here (note older versions of Vundle used Bundle instead of Plugin)
Plugin 'Valloric/YouCompleteMe'
Plugin 'jnurmine/Zenburn' 
Plugin 'altercation/vim-colors-solarized'
Plugin 'jonathanfilip/vim-lucius'
Plugin 'ciaranm/inkpot'
Plugin '29decibel/codeschool-vim-theme'
Plugin 'w0ng/vim-hybrid'
Plugin 'Lokaltog/powerline', {'rtp': 'powerline/bindings/vim/'}
Plugin 'scrooloose/nerdtree'
" Track the engine.
Plugin 'SirVer/ultisnips'
" Snippets are separated from the engine. Add this if you want them:
Plugin 'honza/vim-snippets'
Plugin 'scrooloose/nerdcommenter'
Plugin 'jistr/vim-nerdtree-tabs'
Plugin 'jiangmiao/auto-pairs'
" Bundle 'Raimondi/delimitMate'
" Bundle 'davidhalter/jedi'
Bundle 'davidhalter/jedi-vim'
Plugin 'ervandew/supertab'
Plugin 'tell-k/vim-autopep8'

" All of your Plugins must be added before the following line
call vundle#end()            " required

filetype plugin indent on    " required

"配色方案""""""""""""""""""""""""""""""""""""""""
if has('gui_running') 
	set background=dark 
	colorscheme solarized 
else 
    set background=dark 
    " colorscheme zenburn
    " colorscheme lucius
    " colorscheme inkpot
    colorscheme hybrid
    " colorscheme codeschool
    " colorscheme solarized
endif

"PowerLine 状态栏""""""""""""""""""""""""""""""""""""""""
set nocompatible
set t_Co=256
 
let g:minBufExplForceSyntaxEnable = 1
"python from powerline.vim import setup as powerline_setup
"python powerline_setup()
"python del powerline_setup
 
if ! has('gui_running')
	set ttimeoutlen=10
	augroup FastEscape
		autocmd!
		au InsertEnter * set timeoutlen=0
		au InsertLeave * set timeoutlen=1000
	augroup END
endif
set laststatus=2 " Always display the statusline in all windows
"set guifont=Inconsolata\ for\ Powerline:h14
"set guifont=DejaVu\ Sans\ Mono\ for\ Powerline:h14
set noshowmode " Hide the default mode text (e.g. -- INSERT -- below the statusline)

""""""""""""""""""""""""""""""""""""""""""""""""
" python 虚拟环境
py << EOF
import os
import sys
if 'VIRTUAL_ENV' in os.environ:
    project_base_dir = os.environ['VIRTUAL_ENV']
    activate_this = os.path.join(project_base_dir, 'bin/activate_this.py')
    execfile(activate_this, dict(__file__=activate_this))
EOF

"""""""""""""""""""""""""""""""""""""""""""""""

"标记多余的空格
au BufRead,BufNewFile *.py,*.pyw,*.c,*.h match BadWhitespace /\s\+$/
highlight BadWhitespace ctermbg=red guibg=red

" au BufNewFile,BufRead *.py
" \ set tabstop=4
" \ set softtabstop=4
" \ set shiftwidth=4
" \ set textwidth=79
" \ set expandtab
" \ set autoindent
" \ set fileformat=unix

" 折叠Enable folding 
set foldmethod=indent 
set foldlevel=99
" Enable folding with the spacebar 
" nnoremap <Space> za

"自动注释设置"""""""""""""""""""""""""""""""""""""""
" Add spaces after comment delimiters by default
let g:NERDSpaceDelims = 1
" Use compact syntax for prettified multi-line comments
let g:NERDCompactSexyComs = 1
" Align line-wise comment delimiters flush left instead of following code
" indentation
let g:NERDDefaultAlign = 'left'
" Set a language to use its alternate delimiters by default
let g:NERDAltDelims_java = 1
" Add your own custom formats or override the defaults
let g:NERDCustomDelimiters = { 'c': { 'left': '/**','right': '*/' } }
" Allow commenting and inverting empty lines (useful when commenting a
" region)
let g:NERDCommentEmptyLines = 1
" " Enable trimming of trailing whitespace when uncommenting
let g:NERDTrimTrailingWhitespace = 1

"窗口跳转"""""""""""""""""""""""""""""""""""""""""
" 支持alt+方向键在各个口中切换
map <M-Right> <c-w>l
map <M-Left> <c-w>h
map <M-Up> <c-w>k
map <M-Down> <c-w>j
imap <M-Right> <ESC><c-w>l
imap <M-Left> <ESC><c-w>h
imap <M-Up> <ESC><c-w>k
imap <M-Down> <ESC><c-w>j

" 定义快捷键关闭当前分割窗口 
nmap <Leader>q :q<CR> 

" 定义快捷键保存当前窗口内容 
nmap <Leader>w :w<CR> 
nmap <Leader>wq :wq<CR>

" 定义快捷键保存所有窗口内容并退出 vim 
nmap <Leader>WQ :wa<CR>:q<CR> 

" 不做任何保存，直接退出 vim 
nmap <Leader>Q :qa!<CR>


"split navigations 
" nnoremap <C-J> <C-W><C-J> 
" nnoremap <C-K> <C-W><C-K>
" nnoremap <C-L> <C-W><C-L> 
" nnoremap <C-H> <C-W><C-H>

"树形文件浏览器"""""""""""""""""""""""""""""""""""""""""
" 进入vim没有指定打开文件则打开树形浏览器
autocmd StdinReadPre * let s:std_in=1
autocmd VimEnter * if argc() == 0 && !exists("s:std_in") | NERDTree | endif
" 打开/关闭树形
map <F5> :NERDTreeToggle<CR>
"map <F6> :NERDTreeTabsToggle<CR>
" 切换buffer
"map <C-.> :bprevious<cr>
map <F6> :bnext<cr>

" 关闭最后一个窗口触发关闭vim
autocmd bufenter * if (winnr("$") == 1 && exists("b:NERDTree") && b:NERDTree.isTabTree()) | q | endif
" 设置忽略文件类型" 
let NERDTreeIgnore=['\~$', '\.pyc$', '\.swp$']

"快速注释和反注释""""""""""""""""""""""""""""""""""""""""""
map <S-Down> <s-v>
map <S-Right> <leader>ci<CR>   

"快速测试运行python代码""""""""""""""""""""""""""""""""""""""""
autocmd FileType python nnoremap <buffer> <F12> :w<CR>:!python % <CR>

map <F9> :call RunPython()<CR> 
function RunPython() 
    let mp = &makeprg 
    let ef = &errorformat 
    let exeFile = expand("%:t") 
    setlocal makeprg=python\ -u 
    set efm=%C\ %.%#,%A\ \ File\ \"%f\"\\,\ line\ %l%.%#,%Z%[%^\ ]%\\@=%m 
    silent make % 
    copen 
    let &makeprg = mp 
    let &errorformat = ef 
endfunction

"""""""""""""""""""""""""""""""""""""""""
" Trigger configuration. Do not use <tab> if you use
" https://github.com/Valloric/YouCompleteMe.
"let g:UltiSnipsExpandTrigger="<tab>"
let g:UltiSnipsExpandTrigger="<tab>"
let g:UltiSnipsJumpForwardTrigger="<tab>"
let g:UltiSnipsJumpBackwardTrigger="<s-tab>"
" If you want :UltiSnipsEdit to split your window.
let g:UltiSnipsEditSplit="vertical"

"""""""""""""""""""""""""""""""""""""""
"jedi-vim"""""""""""""""""" 
"ycm的jedi引擎开在开发中，原来的jedi-vim很多特性，
"比如说参数提示、文档实例参看、跳转都还没有支持。
"所以如果想要这些实用的特性我们还要需要安装jedi-vim，配置的时候关闭它的补全功能。
let g:jedi#popup_select_first=0 "弹出选项是不会默认选第一个
let g:jedi#completions_enabled=0 "关闭jedi-vim的补全功能
let g:jedi#auto_vim_configuration=0 "跳过自动配置
let g:jedi#popup_on_dot=0 "关闭句点匹配补全
let g:jedi#completions_command="" "关闭补全命令
let g:jedi#show_call_signatures="1" "貌似是参数提示的选项,2就无法提示参数

"""""""""""""""""""""""""""""""""""""""
"SuperTab
let g:SuperTabDefaultCompletionType = "<C-Tab>"


""""""""""""""""""""""""""""""" 
" => YouCompleteMe Setting 
let g:ycm_key_list_select_completion = ["<C-TAB>", "<Down>"]
let g:ycm_key_list_previous_completion = ["<C-S-TAB>", "<Up>"]

let g:ycm_confirm_extra_conf=0  
let g:ycm_complete_in_comments = 1 
let g:ycm_complete_in_strings = 1 
let g:ycm_collect_identifiers_from_tags_files=1 
let g:ycm_collect_identifiers_from_comments_and_strings = 1 
let g:ycm_seed_identifiers_with_syntax=1 
let g:ycm_collect_identifiers_from_tags_files = 1 
let g:ycm_min_num_of_chars_for_completion=1

let g:ycm_autoclose_preview_window_after_completion=1

let g:ycm_path_to_python_interpreter='/usr/bin/python'

let g:ycm_seed_identifiers_with_syntax=1

"回车即选中当前项
inoremap <expr> <CR> pumvisible() ? '<C-y>' : '<CR>'


" old version 
if !empty(glob("~/.vim/bundle/YouCompleteMe/cpp/ycm/.ycm_extra_conf.py")) 
     let g:ycm_global_ycm_extra_conf ="~/.vim/bundle/YouCompleteMe/cpp/ycm/.ycm_extra_conf.py" 
endif 
" new version 
if  !empty(glob("~/.vim/bundle/YouCompleteMe/third_party/ycmd/cpp/ycm/.ycm_extra_conf.py")) 
     let g:ycm_global_ycm_extra_conf = "~/.vim/bundle/YouCompleteMe/third_party/ycmd/cpp/ycm/.ycm_extra_conf.py" 
endif 

"mapping 
nmap <leader>gd :YcmDiags<CR> 
nnoremap <leader>gl :YcmCompleter GoToDeclaration<CR> 
nnoremap <leader>gf :YcmCompleter GoToDefinition<CR> 
nnoremap <leader>gg :YcmCompleter GoToDefinitionElseDeclaration<CR> 

" 
let g:ycm_filetype_blacklist = { 
        \ 'tagbar' : 1, 
        \ 'gitcommit' : 1, 
        \}
""""""""""""""""""""""""""""""""""


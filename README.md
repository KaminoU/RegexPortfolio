# Regex Portfolio

**Save your useful regex pattern in a portfolio** [Sublime Text][subl].

*This package is written by a lazy dev for lazy dev* =}

Regex pattern could be long and painful to type and test. That's why I want to centralize my fully tested regex in a file that I can reload anytime I need.

[subl]: http://www.sublimetext.com/

## Main features
**5 useful regex** for catching all the :
* changelog
* keywords
* synopsis (desc or description)
* todo
* and all the above keys at the same time

In all the comment style I know. If you have any other useful regex pattern, feel free to share. And do not forget your git username for the credit ;)

![screenshot](https://github.com/KaminoU/regex_portfolio/blob/master/ss/comment_style.png)

**You can also add your custom regex in the Regex Portfolio plugin**
![screenshot](https://github.com/KaminoU/regex_portfolio/blob/master/ss/context_menu.png)

## Documentation
All commands are accessible via the Command Palette, `Ctrl + Shift + P` on Windows/Linux, `Command + Shift + P` on Mac.

![Regex Portfolio](https://github.com/KaminoU/regex_portfolio/blob/master/ss/command_palette.png)

Those commands and your 

The `Find: In...` command opens a quick panel with relevant paths and the ability to filter.

![Find in current file panel](https://f.cloud.github.com/assets/902488/860987/ba97f2b4-f5c2-11e2-9b8d-c53060cd0f59.png)




## Installation
`Regex Portfolio` is available via [Package Control][pkg-ctrl] and can be found as `Regex Portfolio`.

[pkg-ctrl]: http://wbond.net/sublime_packages/package_control

For manual installation, run the following script in the Sublime Text terminal (``ctrl+` ``) which utilizes `git clone` (**you must have git installed**).

```python
import os; path=sublime.packages_path(); (os.makedirs(path) if not os.path.exists(path) else None); window.run_command('exec', {'cmd': ['git', 'clone', 'https://github.com/twolfson/FindPlusPlus', 'Regex Portfolio'], 'working_dir': path})
```

Packages can be uninstalled via `Package Control: Remove Package`, located in the Command Palette.


## License
Copyright (c) 2020 Michel TRUONG

Licensed under the MIT license.

o( ^   ^ )o Cheers!!! o( ^   ^ )o

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

**As you can notice, it's better to terminate the bloc with :::**

The find results will be output in a single file in which all the important information is gathered ^^
![screenshot](https://github.com/KaminoU/regex_portfolio/blob/master/ss/sublime_find_res.png)

## Documentation
### Regex Portfolio
All commands are accessible via the Command Palette, `Ctrl + Shift + P` on Windows/Linux, `Command + Shift + P` on Mac.

![Regex Portfolio](https://github.com/KaminoU/regex_portfolio/blob/master/ss/command_palette.png)

1. `Regex Portfolio: load changelog` to load the changelog regex pattern
2. `Regex Portfolio: load keywords` to load the keywords regex pattern
3. `Regex Portfolio: load synopsis` to load the synospis regex pattern
4. `Regex Portfolio: load todo` to load the todo regex pattern
5. `Regex Portfolio: load all flag (keywords, synopsis, changelog, todo)` to load all the regex pattern at the same time

### User Portfolio (My Regex)
**You can also add your custom regex in the Regex Portfolio plugin**. All your pattern are accessible via the context menu
![screenshot](https://github.com/KaminoU/regex_portfolio/blob/master/ss/context_menu.png)

After loading the wanted regex pattern, select the folder you want to scan.




## Installation
`Regex Portfolio` is available via [Package Control][pkg-ctrl] and can be found as `Regex Portfolio`.

[pkg-ctrl]: http://wbond.net/sublime_packages/package_control

For manual installation, run the following script in the Sublime Text terminal (``ctrl+` ``) which utilizes `git clone` (**you must have git installed**).

```python
import os; path=sublime.packages_path(); (os.makedirs(path) if not os.path.exists(path) else None); window.run_command('exec', {'cmd': ['git', 'clone', 'https://github.com/KaminoU/regex_portfolio.git', 'Regex Portfolio'], 'working_dir': path})
```

Packages can be uninstalled via `Package Control: Remove Package`, located in the Command Palette.


## License
Copyright (c) 2020 宀Кami宀 Michel TRUONG

Licensed under the MIT license.

o( ^   ^ )o Cheers!!! o( ^   ^ )o

# Make changelogs great again

## Usage

```
-c   --commit        Use commit
-t   --tags          Use tags
-a   --author        Show author on commits
Example: gen.py -c/t commit/from_tag,to_tag version version_code
Example: gen.py -c 06141946 0.0.1 001
Example: gen.py -t v0.0.1,v0.0.2 0.0.2 002
```

### Example commit log:
```
commit 2ccd062873b87874427cecb0d3ed1986778348dd
Author: Jeremie Long <jeremie.long@mobiledefense.com>
Date:   Fri Nov 11 16:29:22 2016 -0500

    Update python path
    
    #Fixed fixed the python path for macos

commit 179ea34c8ae1c2b6c54428ee4f0524725930d114
Author: Jeremie Long <jeremie.long@mobiledefense.com>
Date:   Fri Nov 11 15:50:52 2016 -0500

    Add support for comparing changes across tags
    
    #Added tagging support

commit e3b8dac3373dacf9f0c2b305732b47673aa0e1e5
Author: Jeremie Long <jeremie.long@mobiledefense.com>
Date:   Fri Nov 11 14:51:12 2016 -0500

    Print the changelog
    
    #Update updated script to print out to system

commit fe8765a724cfcfd0dd6ae6c23c016bc023d1af6b
Author: Jeremie Long <jeremie.long@mobiledefense.com>
Date:   Fri Nov 11 14:05:57 2016 -0500

    Add initial changelog generation script
    
    #Turtles why the hell not

commit 6bec7ed530cacfa084a7f696d16ba43400d013c6
Author: Jeremie Long <jeremie.long@mobiledefense.com>
Date:   Fri Nov 11 13:20:56 2016 -0500

    Update line one on file
    
    #Fixed Second line has more detail

commit e69b7137a3dfd81338e12c0fff2eb968f5d6df03
Author: Jeremie Long <jeremie.long@mobiledefense.com>
Date:   Fri Nov 11 13:20:15 2016 -0500

    Update line one on file
    
    #Added Update file with a second line

commit 84ef901cc979f9925f50a6beff6660d13a6e0c24
Author: Jeremie Long <jeremie.long@mobiledefense.com>
Date:   Fri Nov 11 13:16:30 2016 -0500

    Update line one on file
    
    #Added Update file with a new line

commit cd5aed685d11d034adc354b3594e4a28a4c524af
Author: Jeremie Long <jeremie.long@mobiledefense.com>
Date:   Fri Nov 11 12:56:07 2016 -0500

    Initial commit

```

### To commit
```
make_changelogs_great_again (master) $ ./gen.py -c 84ef901 0.0.3 003
## 0.0.3 (003) - 14-11-2016
### Turtles
- why the hell not

### Fixed
- fixed the python path for macos
- Second line has more detail

### Added
- tagging support
- Update file with a second line
- Update file with a new line

### Update
- updated script to print out to system
```

### From tag to tag
```
make_changelogs_great_again (master) $ python gen.py -t v0.0.1,v0.0.2 0.0.2 002
## 0.0.2 (002) - 14-11-2016
### Added
- tagging support
```

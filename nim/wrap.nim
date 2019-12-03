import os, strutils, sequtils

proc main(args: seq[string]) =
    if len(args) < 2:
        echo "Wrap long lines in a wide terminal."
        echo "Usage: wrap <column>\nExample: ls -lah | wrap 64"
        quit(0)
    
    let col = args[1].parseInt()

    for each_line in stdin.lines:
        var line = each_line
        while true:
            if col >= line.len():
                echo line
                break
            else:
                echo line[0 .. col - 1]
                line = line[col .. line.len() - 1]

when isMainModule:
    main concat(@[os.getAppFilename()], os.commandLineParams())

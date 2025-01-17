# Write the actual Makefile.

import os


def makemakefile(outfp, makevars, files, target):
    outfp.write("# Makefile generated by freeze.py script\n\n")

    keys = sorted(makevars.keys())
    for key in keys:
        outfp.write("%s=%s\n" % (key, makevars[key]))
    outfp.write("\nall: %s\n\n" % target)

    deps = []
    for i in range(len(files)):
        file = files[i]
        if file[-2:] == '.c':
            base = os.path.basename(file)
            dest = base[:-2] + '.o'
            outfp.write("%s: %s\n" % (dest, file))
            outfp.write("\t$(CC) $(PY_CFLAGS) $(PY_CPPFLAGS) -c %s\n" % file)
            files[i] = dest
            deps.append(dest)

    outfp.write("\n%s: %s\n" % (target, ' '.join(deps)))
    outfp.write("\t$(LINKCC) $(PY_LDFLAGS) $(LINKFORSHARED) %s -o %s $(LDLAST)\n" %
                (' '.join(files), target))

    outfp.write("\nclean:\n\t-rm -f *.o %s\n" % target)

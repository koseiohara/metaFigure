INSTALL = ${HOME}/PythonLib/lib/

ADD = add_pdfinfo.py add_pnginfo.py add_figinfo
GET = figinfo

.PHONY : install uninstall

install :
	cd add; cp ${ADD} ${INSTALL}
	cd get; cp ${GET} ${INSTALL}

uninstall :
	rm -fv ${ADD:%=${INSTALL}%}
	rm -fv ${GET:%=${INSTALL}%}


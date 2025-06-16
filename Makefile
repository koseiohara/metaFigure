INSTALL = ${HOME}/PythonLib/lib/

ADD_MAIN = add_figinfo
ADD = add_pdfinfo.py add_pnginfo.py ${ADD_MAIN} ${ADD_MAIN}.py
GET = figinfo

.PHONY : install uninstall

add/${ADD_MAIN}.py : add/${ADD_MAIN}
	tail -n +2 $^ > $@

install : add/${ADD_MAIN}.py
	cd add; cp ${ADD} ${INSTALL}
	cd get; cp ${GET} ${INSTALL}

uninstall :
	rm -fv ${ADD:%=${INSTALL}%}
	rm -fv ${GET:%=${INSTALL}%}


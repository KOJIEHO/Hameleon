url = document.currentScript.getAttribute('url')
user = document.currentScript.getAttribute('user') + "_update.html?idUser="
fetch(url)
    .then(response => response.json())
    .then(response => 
        $(function (){ 
            tableSettings = response.columns 
            tableData = response.value

            for (i = 0; i < tableSettings.length; i++) {
                if (tableSettings[i].name == "$id"){continue}
                if (tableSettings[i].name[0] == "$"){delete tableSettings.splice(i, 1);i--;}  
            }

            colSettings = [] 
            count = 0
            while (count < tableSettings.length){
                if (tableSettings[count].name){colName = tableSettings[count].name}else{colName = ''}
                if (tableSettings[count].caption){colCaption = tableSettings[count].caption}else{colCaption = ''}
                if (tableSettings[count].type){colType = tableSettings[count].type}else{colType = ''}
                if (tableSettings[count].length){colLenght = tableSettings[count].length}else{colLenght = ''}
                colSettings.push({name: colName, caption: colCaption, type: colType, length: colLenght, align:'center'})
                count++
            }

            key_tableData = Object.keys(tableData[0])
            for (i = 0; i < tableData.length; i++) {
                for (k = 0; k < key_tableData.length; k++){
                    if (key_tableData[k] == "$id"){continue}
                    if (key_tableData[k][0] == "$"){delete tableData[i][key_tableData[k]]}
                }
            }

            "use strict";
                $("#grid").jqGrid({
                    colModel: colSettings,
                    data: tableData,
                    ondblClickRow: function(rowId){
                        var rowData = jQuery(this).getRowData(rowId);
                        window.location.href = user + String(rowData.$id)
                    }
                });
        })   
    )
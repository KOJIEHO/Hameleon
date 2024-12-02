url = 'http://localhost:4388/ham/odata/Prodavec(2001,2002,2003)?$metadata=columns'
fetch(url)
    .then(response => response.json())
    .then(response => 
        $(function () 
        {
            tableSettings = response.columns 
            tableData = response.value

            colSettings = [] 
            count = 0
            while (count < response.columns.length){
                if (tableSettings[count].name){colName = tableSettings[count].name}else{colName = ''}
                if (tableSettings[count].caption){colCaption = tableSettings[count].caption}else{colCaption = ''}
                if (tableSettings[count].type){colType = tableSettings[count].type}else{colType = ''}
                if (tableSettings[count].length){colLenght = tableSettings[count].length}else{colLenght = ''}
                colSettings.push({name: colName, caption: colCaption, type: colType, length: colLenght, align:'center'})
                count++
            }

            "use strict";
                $("#grid").jqGrid({   
                    colModel: colSettings, 
                    data: tableData,
                    ondblClickRow: function(rowId){
                        var rowData = jQuery(this).getRowData(rowId);
                        window.location.href = "prodavec_update.html?idUser=" + String(rowData.ID) + "&fioUser=" + String(rowData.FIO) + "&telefonUser=" + String(rowData.Telefon) + "&prinyatUser=" + String(rowData.Prinyat) + "&dataRogdeniyaUser=" + String(rowData.DataRogdeniya)                       
                    }
                });
        })
    )

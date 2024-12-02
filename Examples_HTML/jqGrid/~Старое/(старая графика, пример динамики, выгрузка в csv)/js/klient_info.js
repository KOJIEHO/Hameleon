fetch('http://localhost:4388/ham/odata/Klient?$expand=pokupki/mashiny,pokupki/prodavec')
    .then(response => response.json())
    .then(response => 
        $(function () 
        {   
            // Динамический вариант \\
            var json = response.value;

            const colName = [{name: 'Num'}];
            for (var x in json[0]){
                if (x[0] != "$"){colName.push({name: x})};                     
            };

            const data = [];
            indexes = Object.keys(json[0]);
            var k = 0;
            while (k < json.length){
                data.push({id: k + 1, Num: k + 1});
                values = Object.values(json[k]);
                var i = 0;             
                for (var x in json[k]){
                    if (x[0] != "$"){
                        data[k][indexes[i]] = values[i];   
                    };
                    i++;
                };
                k++;
            };

            // Тут ниже рабочий варик \\
            // const colName = [
            //     { name: "Num" },
            //     { name: "FIO"},
            //     { name: "Pasport"},
            //     { name: "Orga"},
            //     { name: "Telefon"}
            // ];

            // const data = [];
            // let i = 0;
            // while (i < response.value.length){
            //     data.push({id: i+1, Num: i+1, FIO: response.value[i].FIO, Pasport: response.value[i].Pasport, Orga: response.value[i].Organizaciya, Telefon: response.value[i].Telefon });
            //     i++;
            // };

            "use strict";
                $("#grid").jqGrid({
                    colModel: colName, 
                    data: data
                });
        })
    
    )
    
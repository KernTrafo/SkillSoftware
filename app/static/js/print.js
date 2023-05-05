function printData() {
    var mywindow = window.open('', 'PRINT');
    mywindow.document.write('<html>');
    mywindow.document.write('<head><title>KernTrafo</title></head>');
    mywindow.document.write('<body>');
    mywindow.document.write('<h1>' + document.title  + '</h1>');
    mywindow.document.write('<table class="table"><thead></thead>');

    mywindow.document.write('<tr><td><b>Persönliche Daten</b></td></tr>');
    mywindow.document.write(document.getElementById('persoenlichedatentablebodyoverview').innerHTML);
    mywindow.document.write('<tr><td><b>--------------------------------------------------</b></td></tr>');
    mywindow.document.write('<tr><td><b>Fachliche Qualifikation</b></td></tr>');
    mywindow.document.write(document.getElementById('fachlichequalifikationtablebodyoverview').innerHTML);
    mywindow.document.write('<tr><td><b>--------------------------------------------------</b></td></tr>');
    mywindow.document.write('<tr><td><b>Berufserfahrung</b></td></tr>');
    mywindow.document.write(document.getElementById('berufserfahrungtablebodyoverview').innerHTML);
    mywindow.document.write('<tr><td><b>--------------------------------------------------</b></td></tr>');
    mywindow.document.write('<tr><td><b>Projekterfahrung</b></td></tr>');
    mywindow.document.write(document.getElementById('projekterfahrungtablebodyoverview').innerHTML);
    mywindow.document.write('<tr><td><b>--------------------------------------------------</b></td></tr>');
    mywindow.document.write('<tr><td><b>Abgeschlossene Weiterbildungen</b></td></tr>');
    mywindow.document.write(document.getElementById('weiterbildungentablebodyoverview').innerHTML);
    mywindow.document.write('<tr><td><b>--------------------------------------------------</b></td></tr>');
    mywindow.document.write('<tr><td><b>Geplante Weiterbildungen</b></td></tr>');
    mywindow.document.write(document.getElementById('geplanteweiterbildungentablebodyoverview').innerHTML);
    mywindow.document.write('<tr><td><b>--------------------------------------------------</b></td></tr>');
    mywindow.document.write('<tr><td><b>Gesundheitliche Untersuchungen</b></td></tr>');
    mywindow.document.write(document.getElementById('gesundheitsdatentablebodyoverview').innerHTML);
    mywindow.document.write('<tr><td><b>--------------------------------------------------</b></td></tr>');
    mywindow.document.write('<tr><td><b>Interessen und Sonstiges</b></td></tr>');
    mywindow.document.write(document.getElementById('interessentablebodyoverview').innerHTML);

    mywindow.document.write('</table>');
    mywindow.document.write('</body>');
    mywindow.document.write('</html>');

    mywindow.document.close(); // necessary for IE >= 10
    mywindow.focus(); // necessary for IE >= 10*/

    mywindow.print();
    mywindow.close();

    return true;
};

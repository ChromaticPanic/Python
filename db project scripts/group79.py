import sqlite3
import os
import sys
import csv

if getattr(sys, 'frozen', False):
    dname = os.path.abspath(os.path.dirname(sys.executable))
else:
    dname = os.path.abspath(os.path.dirname(__file__))

os.chdir(dname)
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = os.path.join(dname ,"platforms")
from PySide2.QtWidgets import *
from PySide2.QtSql import *
from PySide2.QtCore import *
from ui_interfacev2 import Ui_MainWindow



db = "Group79.sqlite"


class CONNECTION():
    def __init__(self):
        self.con = sqlite3.connect(os.path.join(dname, db))
        self.cur = self.con.cursor()
        self.quryNum = 99
        self.prevQuery = ""

    def __del__(self):
        self.con.close()

    def send(self, query):
        result = []
        try:
            self.cur.execute(query)
            result.extend(self.cur.fetchall())
            return result
        except Exception as ex:
            print(ex)
            sys.exit(1)

    def sendonly(self, query):
        try:
            self.cur.execute(query)
            return self.cur.fetchone()
            
        except Exception as ex:
            print(ex)
            sys.exit(1)

    def cur(self):
        return self.cur


class AlignDelegate(QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super(AlignDelegate, self).initStyleOption(option, index)
        option.displayAlignment = Qt.AlignCenter


app = QApplication(sys.argv)
window = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(window)
window.show()
con = CONNECTION()


tables = [
        ['age_gender', 'neighbourhood', 'gender', 'age', 'count'],
        ['age_grade', 'age band', 'grade'],
        ['company', 'name', 'loc_id'],
        ['companytransit', 'stop_id', 'company', 'loc_id', 'distance'],
        ['contracts', 'tender', 'amount', 'school', 'company', 'loc_id'],
        ['councilexpenses', 'record', 'councilor', 'date', 'vendor',
         'loc_id', 'type', 'description', 'account', 'amount', 'ward'],
        ['councilmember', 'name', 'ward', 'gender'],
        ['crime', 'record_num', 'neighbourhood',
         'code', 'report_date', 'count'],
        ['crimetype', 'code', 'category', 'offence', 'level3'],
        ['district', 'district_id', 'name', 'area', 'geometry'],
        ['education_age', 'neighbourhood', 'level no certificate age 15-24', 'level no certificate age 25-64', 'level no certificate age over 65', 'level hs certificate age 15-24', 'level hs certificate age 25-64', 'level hs certificate age over 65', 'level trades certificate age 15-24', 'level trades certificate age 25-64', 'level trades certificate age over 65', 'level college age 15-24',
         'level college age 25-64', 'level college age over 65', 'level university all age 15-24', 'level university all age 25-64', 'level university all age over 65', 'level university age 15-24', 'level university age 25-64', 'level university age over 65', 'level master age 15-24', 'level master age 25-64', 'level master age over 65', 'level phd age 15-24', 'level phd age 25-64', 'level phd age over 65'],
        ['education_gender', 'neighbourhood', 'gender', 'degree business', 'degree architecture', 'degree health', 'degree social', 'degree education',
         'degree humanities', 'degree math', 'degree personal', 'degree physical', 'degree visual', 'degree agriculture', 'degree other'],
        ['enrolment', 'name', 'grade', 'count'],
        ['income_gender', 'neighbourhood', 'gender', 'income population all', 'income median all', 'income average all', 'income population full time', 'income median full time', 'income average full time',
         'income population part time', 'income median part time', 'income average part time', 'income population', 'income without income', 'income with income', 'income median income', 'income average income'],
        ['location', 'loc_id', 'geometry', 'address', 'neighbourhood'],
        ['mlacompensation', 'last', 'first', 'base', 'extra', 'other'],
        ['mlacontact', 'last', 'first', 'gender',
         'district', 'party', 'email'],
        ['mlaexpenses', 'last', 'first', 'residence', 'travel',
         'assistant', 'office_rent', 'constituency', 'mail'],
        ['neighbourhood', 'nbhd_id', 'name', 'geometry',
         'ward', 'schooldiv', 'district'],
        ['park', 'park_id', 'name', 'water_area_hect',
         'land_area_hect', 'loc_id'],
        ['parkasset', 'asset_id', 'park_id', 'class', 'type', 'loc_id'],
        ['parktransit', 'stop_id', 'park_id', 'distance'],
        ['routes', 'stop_id', 'route_id'],
        ['school', 'name', 'loc_id'],
        ['schooldivision', 'division_id', 'name', 'website', 'geometry'],
        ['schooltransit', 'stop_id', 'schoolname', 'distance'],
        ['sequentialenrolment', 'hs_name', 'ps_name', 'count'],
        ['stops', 'stop_id', 'name', 'loc_id'],
        ['tree', 'tree_id', 'botanical_name',
         'diameter', 'park_id', 'loc_id'],
        ['treename', 'botanical', 'common'],
        ['ward', 'ward_id', 'name', 'geometry']
    ]
queries = [
    """select d.name, sum(ig."income median full time") / count(ig.neighbourhood) as "average full time median income" from district d
        inner join neighbourhood n on d.name = n.district
        inner join income_gender ig on n.name = ig.neighbourhood
        group by d.name
        order by "average full time median income" DESC;""",

    """select n.name, sum(a.tc) as "Total Crime", sum(b.tp) as "Total Population", printf("%.4f",cast(sum(a.tc) as real)/cast(sum(b.tp) as real)) as "Crimes per capita" from
        (select c.neighbourhood, sum(c.count) as tc from crime c group by c.neighbourhood) as a
            inner join
                (select ag.neighbourhood, sum(ag.count) as tp from age_gender ag group by ag.neighbourhood) as b
            on a.neighbourhood = b.neighbourhood
        inner join neighbourhood n on n.name = a.neighbourhood
        group by n.district
        order by "Crimes per capita" DESC ;""",

    """select ward, sum(a.tc) as "Tree Count", sum(b.tp) as Population,
            printf("%.0f",cast(sum(c.mi) as real)/cast(count(a.neighbourhood) as real)) as "Avg Median FT income",
            printf("%.4f",cast(sum(a.tc) as real)/cast(sum(b.tp) as real)) as "Trees per capita" from
        (select l.neighbourhood, count(t.tree_id) as tc from tree t
            inner join location l on l.loc_id = t.loc_id
            group by l.neighbourhood) as a
        inner join
            (select ag.neighbourhood, sum(ag.count) as tp from age_gender ag group by ag.neighbourhood) as b
            on a.neighbourhood = b.neighbourhood
        inner join
            (select ic.neighbourhood, cast(sum(ic."income median full time") as real)/2.0 as mi from income_gender ic group by ic.neighbourhood) as c
            on c.neighbourhood = a.neighbourhood
        inner join neighbourhood on a.neighbourhood = neighbourhood.name
        group by ward
        order by "Trees per capita" DESC ;""",

    """
        select * from
        (select c.neighbourhood, top."advanced degree holders",count(c2.offence) as incidents, c2.offence, c2.level3 from crime c inner join
            (select name,
                (sum("level master age 15-24") + sum("level master age 25-64") + sum("level master age over 65") +
                sum("level phd age 15-24") + sum("level phd age 25-64") + sum("level phd age over 65")) as "advanced degree holders" from neighbourhood
                inner join education_age ea on neighbourhood.name = ea.neighbourhood
                group by name
                order by "advanced degree holders" DESC limit 1) as top
            on neighbourhood = top.name
            inner join crimetype c2 on c2.code = c.code
            group by c.neighbourhood, c2.offence
            order by incidents DESC limit 5)
        union
        select * from
        (select c.neighbourhood, top."advanced degree holders",count(c2.offence) as incidents, c2.offence, c2.level3 from crime c inner join
            (select name,
                (sum("level master age 15-24") + sum("level master age 25-64") + sum("level master age over 65") +
                sum("level phd age 15-24") + sum("level phd age 25-64") + sum("level phd age over 65")) as "advanced degree holders" from neighbourhood
                inner join education_age ea on neighbourhood.name = ea.neighbourhood
                group by name
                order by "advanced degree holders" DESC limit 1 offset 1) as top
            on neighbourhood = top.name
            inner join crimetype c2 on c2.code = c.code
            group by c.neighbourhood, c2.offence
            order by incidents DESC limit 5)
        union
        select * from
        (select c.neighbourhood, top."advanced degree holders",count(c2.offence) as incidents, c2.offence, c2.level3 from crime c inner join
            (select name,
                (sum("level master age 15-24") + sum("level master age 25-64") + sum("level master age over 65") +
                sum("level phd age 15-24") + sum("level phd age 25-64") + sum("level phd age over 65")) as "advanced degree holders" from neighbourhood
                inner join education_age ea on neighbourhood.name = ea.neighbourhood
                group by name
                order by "advanced degree holders" DESC limit 1 offset 2) as top
            on neighbourhood = top.name
            inner join crimetype c2 on c2.code = c.code
            group by c.neighbourhood, c2.offence
            order by incidents DESC limit 5)
            order by neighbourhood, incidents DESC;""",

    """select company, printf("%.2f",a."total award") as "total award ($)", b.name as "neighbourhood", b."fraud incidents" from company c inner join
        (select ct.company, cast(sum(ct.amount) as real) as "total award", ct.loc_id from contracts ct
            where ct.school like 'university of manitoba'
            group by ct.company
            order by "total award") as a
        on c.name = a.company and a.loc_id = c.loc_id
        inner join location l on l.loc_id = c.loc_id
        inner join neighbourhood n on l.neighbourhood = n.name
        inner join
            (select n2.name, count(c3.offence) as "fraud incidents" from crime c2
                inner join neighbourhood n2 on c2.neighbourhood = n2.name
                inner join crimetype c3 on c2.code = c3.code
                group by neighbourhood) as b
        on n.name = b.name
        order by a."total award" DESC;""",

    """select sd.name as "School Division", count(distinct a.route_id) as "bus route count"from schooldivision sd
        inner join
        (select n.name, r.route_id, n.schooldiv from routes r
            inner join stops s on s.stop_id = r.stop_id
            inner join location l on l.loc_id = s.loc_id
            inner join neighbourhood n on l.neighbourhood = n.name
            group by n.name) as a
        on sd.name = a.schooldiv
        group by sd.name
        order by "bus route count" DESC ;""",

    """select w.name, printf("%.2f",a."Total Park Area") as "Total Park Area",
        printf("%.2f",a.wa) as "Water Area Hectares",
        printf("%.2f",a.la) as "Land Area Hectares",
        printf("%.2f",cast(sum(a."income median full time") as real)/cast(count(a.name) as real)) as "average median full time income"
        from ward w
        inner join
        (select n.name, sum(p.water_area_hect) as wa, sum(p.land_area_hect) as la,
            (sum(p.water_area_hect) + sum(p.land_area_hect)) as "Total Park Area", n.ward, ig."income median full time"
            from park p
            inner join location l on l.loc_id = p.loc_id
            inner join neighbourhood n on n.name = l.neighbourhood
            left join income_gender ig on n.name = ig.neighbourhood
            group by n.name) as a
        on a.ward = w.name
        group by w.name
        order by a."Total Park Area" DESC ;""",

    """select ward, count(botanical_name) as "solo trees" from
        (select ward, botanical_name, count(botanical_name) as num from tree t
            inner join treename t2 on t.botanical_name = t2.botanical
            inner join location l on l.loc_id = t.loc_id
            inner join neighbourhood n on n.name = l.neighbourhood
            group by n.ward, botanical_name
            having num = 1 ) as a
        group by ward;""",

    """
        select * from
            (select c.neighbourhood, top."tree count",count(c2.offence) as incidents, c2.offence, c2.level3 from crime c inner join
                (select name, (count(t.tree_id)) as "tree count" from neighbourhood
                    inner join location l on neighbourhood.name = l.neighbourhood
                    inner join tree t on l.loc_id = t.loc_id
                    group by name
                    order by "tree count" DESC limit 1 offset 0) as top
                on neighbourhood = top.name
                inner join crimetype c2 on c2.code = c.code
                group by c.neighbourhood, c2.offence
                order by incidents DESC limit 5)
            union
            select * from
                (select c.neighbourhood, top."tree count",count(c2.offence) as incidents, c2.offence, c2.level3 from crime c inner join
                    (select name, (count(t.tree_id)) as "tree count" from neighbourhood
                        inner join location l on neighbourhood.name = l.neighbourhood
                        inner join tree t on l.loc_id = t.loc_id
                        group by name
                        order by "tree count" DESC limit 1 offset 1) as top
                    on neighbourhood = top.name
                    inner join crimetype c2 on c2.code = c.code
                    group by c.neighbourhood, c2.offence
                    order by incidents DESC limit 5)
            union
            select * from
                (select c.neighbourhood, top."tree count",count(c2.offence) as incidents, c2.offence, c2.level3 from crime c inner join
                    (select name, (count(t.tree_id)) as "tree count" from neighbourhood
                        inner join location l on neighbourhood.name = l.neighbourhood
                        inner join tree t on l.loc_id = t.loc_id
                        group by name
                        order by "tree count" DESC limit 1 offset 2) as top
                    on neighbourhood = top.name
                    inner join crimetype c2 on c2.code = c.code
                    group by c.neighbourhood, c2.offence
                    order by incidents DESC limit 5)
            union
            select * from
                (select c.neighbourhood, top."tree count",count(c2.offence) as incidents, c2.offence, c2.level3 from crime c inner join
                    (select name, (count(t.tree_id)) as "tree count" from neighbourhood
                        inner join location l on neighbourhood.name = l.neighbourhood
                        inner join tree t on l.loc_id = t.loc_id
                        group by name
                        order by "tree count" DESC limit 1 offset 3) as top
                    on neighbourhood = top.name
                    inner join crimetype c2 on c2.code = c.code
                    group by c.neighbourhood, c2.offence
                    order by incidents DESC limit 5)
            union
            select * from
                (select c.neighbourhood, top."tree count",count(c2.offence) as incidents, c2.offence, c2.level3 from crime c inner join
                    (select name, (count(t.tree_id)) as "tree count" from neighbourhood
                        inner join location l on neighbourhood.name = l.neighbourhood
                        inner join tree t on l.loc_id = t.loc_id
                        group by name
                        order by "tree count" DESC limit 1 offset 4) as top
                    on neighbourhood = top.name
                    inner join crimetype c2 on c2.code = c.code
                    group by c.neighbourhood, c2.offence
                    order by incidents DESC limit 5)
            order by "tree count" DESC, incidents DESC;""",

    """select * from ward;""",
    """select * from ward;""",
    
    """select m2.last, m2.first, m.district, m2.extra, m.party, a."average full time median income" from
        (select d.name, sum(ig."income median full time") / count(ig.neighbourhood) as "average full time median income" from district d
                inner join neighbourhood n on d.name = n.district
                inner join income_gender ig on n.name = ig.neighbourhood
                group by d.name
                order by "average full time median income" DESC) as a
        inner join mlacontact m on m.district = a.name
        inner join mlacompensation m2 on m.last = m2.last and m.first = m2.first
        where m2.extra > a."average full time median income";""",

    """select * from
        (select a.neighbourhood, a."pop total hs age", sum(e.count) as "pop in hs", a."pop total hs age" - sum(e.count) as "not enrolled" from
            (select ag2.neighbourhood, sum(ag2.count) as "pop total hs age" from age_gender ag2 where ag2.age in
                (select distinct ag."age band" from age_grade ag
                    where ag.grade like 'nine' or ag.grade like 'ten' or ag.grade like 'eleven' or ag.grade like 'twelve')
                group by ag2.neighbourhood) as a
            inner join location l on l.neighbourhood = a.neighbourhood
            inner join school s on l.loc_id = s.loc_id
            inner join enrolment e on s.name = e.name
            where e.grade like 'nine' or
                        e.grade like 'ten' or
                        e.grade like 'eleven' or
                        e.grade like 'twelve'
                    group by s.name
            having "pop in hs" > 0)
        where "not enrolled" > 0
        group by neighbourhood
        order by "not enrolled" DESC ;""",

    """Select a.name as neighbourhood, group_concat(p.name) parks  from
        (select * from neighbourhood n2
            where n2.name not in
            (select hs.name from
                (select s.name as hs, sum(e.count) as "HS students", n.name from neighbourhood n
                    inner join location l on n.name = l.neighbourhood
                    inner join school s on l.loc_id = s.loc_id
                    inner join enrolment e on s.name = e.name
                    where e.grade like 'nine' or
                        e.grade like 'ten' or
                        e.grade like 'eleven' or
                        e.grade like 'twelve'
                    group by s.name
                    having "HS students" > 0) as hs)) as a
        inner join location l2 on a.name = l2.neighbourhood
        inner join park p on l2.loc_id = p.loc_id
        group by neighbourhood;""",

    """Select a.name as neighbourhood, a.robberies, group_concat(distinct r.route_id) routes from
            (select n.name, count(c2.offence) as robberies from neighbourhood n
                inner join crime c on n.name = c.neighbourhood
                inner join crimetype c2 on c2.code = c.code
                where c2.offence like 'robbery'
                group by n.name) as a
            inner join location l on a.name = l.neighbourhood
            inner join stops s on l.loc_id = s.loc_id
            inner join routes r on s.stop_id = r.stop_id
            group by a.name, a.robberies
            order by robberies DESC limit 10;""",

    """select a.name as district, a."average full time median income", b."play structures" from
        (select d.name, sum(ig."income median full time") / count(ig.neighbourhood) as "average full time median income" from district d
            inner join neighbourhood n on d.name = n.district
            inner join income_gender ig on n.name = ig.neighbourhood
            group by d.name
            order by "average full time median income" DESC) as a
        inner join
            (select d2.name, count(pa.class) as "play structures" from parkasset pa inner join location l on pa.loc_id = l.loc_id
                inner join neighbourhood n2 on l.neighbourhood = n2.name
                inner join district d2 on n2.district = d2.name
                where pa.class like 'stand alone play component'
                group by d2.name) as b
        on a.name = b.name;"""
]

def main():
    

    ui.spinBox.setValue(100)
    ui.comboBox_tables.addItems([item[0] for item in tables])
    ui.showTableButton.clicked.connect(showTable)
    ui.queryButton.clicked.connect(runQuery)
    ui.nextButton.clicked.connect(getNext)
    ui.exportButton.clicked.connect(dumpToCsv)

    sys.exit(app.exec_())


def dumpToCsv():
    out = "tabledump.csv"
    inc = 0
    result = ""
    while os.path.exists(out):
        inc += 1
        out = "tabledump" + str(inc) + ".csv"
        
    with open(os.path.join(dname, out), "w", newline="") as f:
        writer = csv.writer(f)
        if con.queryNum == 99:
            name = ui.comboBox_tables.currentText()
            result = con.send("select * from " + name + ";")
        else:
            result = con.send(con.prevQuery)

        writer.writerow(get_col_names())
        for row in result:
            writer.writerow(row)


def runQuery():
    ui.tableWidget.clear()
    name = ""
    for widget in ui.tab_query.findChildren(QRadioButton):
        if widget.isChecked():
            name = widget.objectName()
            break
    con.queryNum = int(name.split("y")[1]) - 1

    if con.queryNum != 99:
        limit = ui.spinBox.value()
        con.prevQuery = queries[con.queryNum]

        updateRows(con.prevQuery)
        result = con.sendonly(con.prevQuery)
        setTable(limit, len(result))

        ui.tableWidget.horizontalHeader().setDefaultAlignment(Qt.AlignLeft | Qt.Alignment(Qt.TextWordWrap))

        for column, col in enumerate(result):
            ui.tableWidget.setItem(0, column, QTableWidgetItem(str(col)))
        for row in range(1,limit):
            result = con.cur.fetchone()
            if result:
                for column, col in enumerate(result):
                    ui.tableWidget.setItem(row, column, QTableWidgetItem(str(col)))
            else:
                break
    
        ui.tableWidget.resizeColumnsToContents()
        
def showTable():
    ui.tableWidget.clear()
    name = ui.comboBox_tables.currentText()

    if name:
        limit = ui.spinBox.value()
        con.prevQuery = "select * from " + name + ";"
        con.queryNum = 99
        updateRows(con.prevQuery)
        result = con.sendonly(con.prevQuery)
        setTable(limit, len(result))

        ui.tableWidget.horizontalHeader().setDefaultAlignment(Qt.AlignLeft | Qt.Alignment(Qt.TextWordWrap))
        
        for column, col in enumerate(result):
            ui.tableWidget.setItem(0, column, QTableWidgetItem(str(col)))
        for row in range(1,limit):
            result = con.cur.fetchone()
            if result:
                for column, col in enumerate(result):
                    ui.tableWidget.setItem(row, column, QTableWidgetItem(str(col)))
            else:
                break
    
        ui.tableWidget.resizeColumnsToContents()
        
        # delegate = AlignDelegate(ui.tableWidget)
        # ui.tableWidget.setItemDelegate(delegate)

def getNext():
    ui.tableWidget.clear()
    limit = ui.spinBox.value()
    for row in range(limit):
        result = con.cur.fetchone()
        if result:
            for column, col in enumerate(result):
                ui.tableWidget.setItem(row, column, QTableWidgetItem(str(col)))
        else:
            break
    ui.tableWidget.resizeColumnsToContents()
    return

def setTable(row, col):
    ui.tableWidget.setRowCount(row)
    ui.tableWidget.setColumnCount(col)
    ui.tableWidget.setHorizontalHeaderLabels(get_col_names())


def get_col_names():
    #con.cur.execute(query + " limit 1;")
    return [member[0] for member in con.cur.description]

def updateRows(query):
    result = con.send(" select count (*) from (" + query[:-1] + ");")
    ui.label_totalRows.setText(str(result[0][0]))
    return

if __name__ == "__main__":
    main()

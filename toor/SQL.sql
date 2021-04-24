-- 数据库的操作
windows下手动启动mysql服务  win+r  输入services.msc 找到mysql服务属性启动

    -- 链接数据库
    mysql -uroot -p
    mysql -uroot -p+密码

    -- 退出数据库
    exit / ctrl + D / quit

    -- 显示当前所有数据库
    show databases;

    -- 显示数据库当前时间
    select now();

    -- 显示数据库当前版本
    select version();

    -- 创建数据库
    create database 数据库名 charset=utf8;

    -- 删除数据库
    drop database 数据库

    -- 查看数据库创建的语句
    show create database 数据库名;


    -- 查看当前使用的数据库
    select database();
    select daatabase();

    -- 使用一个数据库
    use 数据库名;

********************************************************************************************

-- 操作数据库表

    -- 查看数据库表
    show tables;

    -- 查看数据库表结构
    desc 表名;
    desc 表名;

    -- 创建数据表
    create table 表名(字段,类型,约束)

    create table students(
    id int unsigned not null auto_increment primary key ,
    name varchar(30),
    age tinyint unsigned,
    high decimal(5,2),
    gender enum("男","女","中性","保密") default "保密",
    cls_id int unsigned
    );

    -- 修改表结构(添加字段)
    alter table 表名 add 列名 类型;
    alter table students add birthday datetime;

    -- 修改字段（不重名版）
    alter table 表名 modify 列名 类型 约束;
    alter table students modify birthday date;
    alter table students modify gender enum("男","女") default "女";

    -- 修改字段（重名版）
    alter table 表名 change 原名 新名 类型和约束;
    alter table students change birthday birth date default "2020-04-28";

    -- 删除字段
    alter table 表名 drop 字段;

********************************************************************************************************

-- 数据库表的数据操作(增 删 改 查 curd )

mysql> desc students;
+--------+---------------------+------+-----+------------+----------------+
| Field  | Type                | Null | Key | Default    | Extra          |
+--------+---------------------+------+-----+------------+----------------+
| id     | int(10) unsigned    | NO   | PRI | NULL       | auto_increment |
| name   | varchar(30)         | YES  |     | NULL       |                |
| age    | tinyint(3) unsigned | YES  |     | NULL       |                |
| high   | decimal(5,2)        | YES  |     | NULL       |                |
| gender | enum('0','1')       | YES  |     | 0          |                |
| cls_id | int(10) unsigned    | YES  |     | NULL       |                |
| birth  | date                | YES  |     | 2020-04-28 |                |
+--------+---------------------+------+-----+------------+----------------+

    -- 增加数据(需 一一对应)
    -- 全部插入
    -- 主键字段 可以用 0 ，null , default 来占位
    -- 向 classes表中插入数据
    insert into classes values(1,"精英班"),(2,"王者班")

    -- 向students 表中插入学生信息
    insert into students values(0,"王五",18,160.00,2,1,"2005-01-18");

    -- 部分插入 (带上字段)
    insert into 表名 (列名1,...) values (值1,...);
    insert into students (name,age,high,gender) values("狗杂",20,165.02,1);

    -- 多行插入 值后面添加 逗号和空格
    insert into students (name,age,high) values("王牌",20,165.02), ("大菠萝",11,123.45);

    -- 修改 使用update
    update 表名 set 列1=值1, 列2=值2,...where 条件;
    update students set gender="女" , cls_id=1 where name="大菠萝";

    -- 查询
    -- 查找所有
    select * from 表名;

    -- 指定条件查询
    select * from 表名 where 条件l;

    -- 查询指定列 并重命名列
    select 列1 as 列1新名, 列2 as 列2新名,.... from 表名;
    select name as "姓名", gender as "性别" from students;

    -- 删除数据
    -- 删除整个表数据
    delete from students;

    -- 物理删除 和 逻辑删除
    -- 物理删除是真正的删除，一般使用逻辑删除   数据来之不易，切记！！！
    -- 用一个字段来表示这条信息是否已经不能再用了
    -- 给 students 表添加一个is_delete 字段 bit 类型
    alter table students add is_delete bit default 0;
    update students set is_delete=1 where id=2;

**********************************************************************************************************
******************************数据库的数据查询详解********************************************************

-- SQL查询
-- 基本查询
        -- 数据准备，创建数据库，使用数据库，创建表，添加字段和数据
        -- 查询所有字段
        -- 查询指定字段
        -- 使用as 起别名, 给表起别名需要用别名，原名不能用
        -- 消除重复行 distinct
        select distinct name from students;  -- 去掉重复的名字

-- 条件查询
        -- 比较运算符
        -- and ,or
        -- 查询16岁以上或者身高小于150cm的名字
        select name from students where age>16 or high<150;

        -- not
        -- 查询不在18岁女性这个范围的信息
        select * from students where not (age=18 and gender="女");

        -- 年龄不是小于 或者等于20 并且是女性
        select * from students where not (age<=20 and gender="女");


 -- like 模糊查询
        -- % 替换一个或者多个
        -- _ 替换一个

        -- 查询姓名中有 菠 的所有名字
        select name from students where name like "%菠%";
        select name from students where name REGEXP "^b";

        -- 查询有三个字的名字
        select name from students where name like "___";

        -- 查询至少两个字的名字
        select name from students where name like "__%";

        -- rlike 正则
        -- 查询以 王 开始的姓名
        select name from students where name rlike "^王.*";

        -- 查询以 大 开头 萝 结尾的姓名
        select name from students where name rlike "^大.*萝$";

 -- 范围查询
        -- in (1,3,6)表示在一个非连续的范围里
        -- 查询年龄为11 ，20的姓名
        select name from students where age in (11,20);

        -- not in () 不在括号内的
        select name from students where age not in (11,20);

        -- between....and.... 表示某范围 和某范围之间
        -- 查询年龄在10 到30 之间的信息
        select  * from students where age between 10 and 30;

        -- not between... and ...

        -- 空判断
        -- 判空 is null ； 非空 is not null
        -- 查询 身高 为空的信息
        select * from students where high is null;

-- 排序查询  （order by 字段）
    -- asc 升序
    -- 查 询年龄在18 -30 岁之间的男性，按照年龄升序排列
    select * from students where (age between 18 and 30) and gender = "男" order by  age asc;

    -- desc 降序
    -- 查 询年龄在18 -30 岁之间的女性，按照 年龄 降序排列, 若年龄相同按照 id 降序排列
    select * from  students where (age between 10 and 30) and gender="女" order by age desc,id desc;

-- 聚合函数
    -- 总数 count
    -- 查询男性有多少人，女性有多少人
    select count(*) as "男性人数" from students where gender="男" ;
    select count(*) as "女性人数" from students where gender="女" ;

    -- 最大值 max
    -- 求最大的年龄
    select max(age) from students where age;
    select name,max(high) from students where gender=2;

    -- 最小值 min
    -- 求和 sum
    -- 平均 avg
    -- 计算平均年龄
    select sum(age)/count(*) from students;

    -- 四舍五入 round(123.231,1) 保留以为小数
    -- 计算所有人的平均年龄，保留两位小数
    select round(sum(age)/count(*),2) from students ;
    select round(sum(high)/count(*),2) from students where gender="男";

-- 分组查询 和 聚合函数 一起使用
    -- group by 先分组 然后再从组里的数据计算
    -- 查询 男，女的人数； 添加where 条件时只能放在group by 前面
    select gender,count(*) from students group by gender;
    select gender,count(*) from students where gender=1 group by gender;

    -- 通过group_concat(字段1，字段2...)查看分组中的字段信息
    select gender as "性别",count(*) as "总人数",group_concat(name,"-",age) as "详细信息" from students where gender=1 group by gender;

    -- having 过滤  区别 having 在group by 后面 ，是对查询结果的过滤
    -- 查询平均年龄超过18岁的性别，以及姓名
    select gender,group_concat(name) from students group by gender having avg(age>18);


-- 分页查询  limit(第n页-1)* 每页的个数 且limit必须放最后面
    -- limit 2   限制查询出来的数据个数只能是2个
    select * from students limit 3;

    -- limit 0,5  查询某位置开始的几条数据; 0 表示从头开始，5 表示5条数据
    select * from students limit 3,5;

    -- 查询所有女性学生 按身高的降序排列且每次显示两个
    select * from students where gender=2 order by high desc  limit 0,2;


-- 连接查询
mysql> select * from classes;
+----+-----------+
| id | name      |
+----+-----------+
|  1 | 菜鸟班    |
|  2 | 精英班    |
|  3 | 王者班    |
+----+-----------+
3 rows in set (0.00 sec)
mysql> select * from students;
+----+-----------+------+--------+--------+--------+------------+-----------+
| id | name      | age  | high   | gender | cls_id | birth      | is_delete |
+----+-----------+------+--------+--------+--------+------------+-----------+
|  1 | 张三      |   18 | 160.00 | 男     |      1 | 2002-01-08 |           |
|  2 | 李四      |   18 | 160.00 | 男     |      1 | 2002-01-08 |           |
|  3 | 王五      |   18 | 160.00 | 男     |      1 | 2005-01-18 |           |
|  4 | 狗杂      |   20 | 165.02 | 女     |      1 | 2020-04-28 |           |
|  7 | 王牌      |   20 | 165.02 | 女     |      1 | 2020-04-28 |           |
|  8 | 大菠萝    |   11 | 123.45 | 女     |      1 | 2020-04-28 |           |
|  9 | 王牌      |   20 | 165.02 | 女     |      2 | 2020-04-28 |           |
| 10 | 大菠萝    |   11 | 123.45 | 女     |      3 | 2020-04-28 |           |
| 11 | 王牌      |   20 | 165.02 | 女     |      2 | 2020-04-28 |           |
| 12 | 大菠萝    |   11 | 123.45 | 女     |      2 | 2020-04-28 |           |
+----+-----------+------+--------+--------+--------+------------+-----------+

    -- 内连接  表1 inner join 表2.. on.条件.. 两张关联表都有数据
    -- 查询有能够对应上班级的学生以及班级信息
    select * from students inner join classes on students.cls_id = classes.id;

    -- 按照要求显示姓名、班级
    select students.name,classes.name from students inner join classes on students.cls_id=classes.id;

    -- 将班级姓名显示在第一列，显示相应的学生信息 按班级id排序，若属于同一班级则按学生id降序排列
    select classes.name,students.* from students inner join classes on students.cls_id = classes.id order by classes.id,students.id desc;

    -- 外连接 左连接 和 右连接
    -- 查询每位学生对应的班级信息
    select students.* from students left join classes on students.cls_id=classes.id;

    -- 右连接  将表名对换位置 用left join on 实现
    select students.* from classes left join students on students.cls_id=classes.id;

    -- 查询没有对应班级关系的学生
    select * from students left join classes on students.cls_id=classes.id having classes.id is null;

-- 自关联  一个表的字段 关联 该表 的另一个字段
    -- 全国三级城市联动 数据表设计

    -- 如何将sql 数据导入到 数据表中
        -- 1.退出mysql数据库
        -- 2.将xxx.sql 文件放到当前数据库执行文件下，用pwd 查看当前路径
        -- 3.登录数据库，使用数据库查看表，里面会有xxx表
        -- 4.source xxx.sql 即可导入

-- 子查询
    -- 查询最高的男生的信息
    select * from students where high = (select max(high) from students );

-- 数据库设计 (主要的是数据表)
    -- 三范式
    -- (1NF)：原子性  既不能在拆分
    -- (2NF)：必须有主键，其它字段必须直接依赖于主键
    -- (3NF)：非主键列必须直接依赖于主键，不能存在传递依赖；即不能存在 非主键A依赖非主键列B，非主键B依赖主键

    -- E-R 模型
    -- 一对一 ：一个表的一条记录对应另一个表的一条记录
    -- 多对一 ：一个表的多条记录 对应 另一个表的一条记录；必须在 多的记录的表里新建一个字段存储一的主键
    -- 多对多 ：新开一个表存贮两个表的主键，称为聚合表

-- json数据存储到数据库
create table testdata(
    id int(10) unsigned not null auto_increment,
    payload json default null ,
    response json default null,
    primary key (id)

)engine=InnoDB default charset=utf8

-- 为方便快速插入千万条测试数据、等我们插完数据再把存储类型改为InnoDB
-- show ENGINES;

DROP TABLE IF EXISTS big_data;
CREATE TABLE big_data(
id int PRIMARY KEY NOT NULL AUTO_INCREMENT,
name1 varchar(16) default null ,
age int(11),
email varchar(64) default null
)ENGINE=MYISAM DEFAULT CHARSET=utf8;

DROP PROCEDURE if exists inser_data_pro;

DELIMITER $$
CREATE PROCEDURE insert_data_pro()
    begin
        declare i int;
        set i=0;
        while i>=0 && i<=100000 DO INSERT INTO big_data(name1, age, email) values(concat('linda', i), rand()*50, concat('linda', i, 'qq.com'))
        end while;
        end $$
DELIMITER ;

call insert_data_pro();
alter TABLE `big_data` engine=innodb;
alter table big_data engine=myisam;

-- 如何写SQL语句

select name from table group by name having min(fenshu)>=60
-- 一、查询”01“的课程比02的课程成绩高的学生信息和课程分数
select a.*, b.score 课程01的分数, c.score 课程02的分数  from students a, SC b, SC c where a.SID = b.SID and  a.SID=c.SID
and b.CID = '01' and c.CID='02' and b.score > c.score
-- 1、写出所有要查询的信息 select a.*, b.score 课程01的分数, c.score 课程02的分数
-- 2、from 这些信息所在的表from students a, SC b, SC c
-- 3、这些表的关联字段进行条件设置

-- 二、 查询同时存在01课程和02课程 和存在01课程但可能不存在02课程的情况(不存在时显示为NULL)的学生信息和课程分数
select students.*, b.score 课程01的分数, c.score 课程02的分数 from students a
left join SC b on a.SID = b.SID and b.CID='01'
left join SC c on a.SID = c.SID and c.CID='02'
where b.score > isnull(c.score)

-- 三、 查询01课程比02课程成绩低的学生的信息及课程分数
-- 1、所引用到的表  students  as s , course as c ， 成绩表 SC
select s.* , b.score 课程01的分数, c.score 课程2的分数 from students a, SC b, SC c
where b.score < c.score and s.SID=b.SID and a.SID=c.SID and b.CID='01' and c.CID='02'

-- 四、查询平均成绩大于60分的同学的学生编号和学生姓名和平均成绩
-- 1、cast()表达式的用法  将小数5.214785412转化为标准小数比如5.21  cast(avg(10/3) as decimal(9,2)) 9代表最大支持数，2代表小数位数
select s.SID, s.Sname, cast(avg(b.score) as decimal(9,2))  avg_score from students s, SC b where s.SID = b.SID
group by s.SID,s.Sname having cast(avg(b.score) as decimal(9,2)) >=60 order by s.SID

-- 五、查询在SC表中不存在成绩的学生信息的SQL语句
select s.SID, s.Sname, cast(avg(b.score) as decimal(9,2))  avg_score from students s left join SC b on s.SID = b.SID
group by s.SID,s.Sname having cast(avg(b.score) as decimal(9,2)) =0 order by s.SID

-- 六、查询所有同学的学生编号、学生姓名、选课总数、所有课程的总成绩
select a.SID 学生编号, a.Sname 学生姓名, count(b.CID) 选课总数, sum(score) 所有课程总成绩 from students a, SC b
where a.SID = b.SID group by a.SID, a.Sname order by a.SID

-- 七、查询所有的包括有成绩、无成绩的SQL
select a.SID 学生编号, a.Sname 学生姓名, count(b.CID) 选课总数, sum(score) 所有课程总成绩 from students a left join SC b on a.SID = b.SID
group by a.SID, a.Sname order by a.SID

-- 八、查询”李“姓老师的数量  %表示%前面有一个李字
select count(Tname) from Teacher where Tname="李%"
select count(Tname) from Teacher where left(Tname,1) = '李'  left的用法 从左边返回第一个字符串1表示第一个

-- 九、查询学过"张三"老师授课的同学的信息
select a.* from students a ,Teacher b, Course c, SC e where e.SID=a.SID and c.CID=e.CID and c.TID=b.TID and b.Tname="张三" order by a.SID +

-- 十、查询学过编号为01并且也学过编号02的课程的同学的信息
select a.* from students a, SC b, Course c GROUP BY a.SID where a.SID=b.SID and b.CID=c.CID having c.CID='01'and c.CID='02'

select m.students  from students m where SID in (select SID from (select distinct SID from SC where CID='01' union all select distinct SID from SC where CID='02') )

-- 十一、查询两门及其以上不及格课程的同学的学号、姓名、及其平均成绩
select s.SID 学号, s.Sname 姓名, avg_score 平均成绩 from  students s ,

















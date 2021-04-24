create table fenshu(
    id int unsigned not null auto_increment primary key,
    name varchar(30),
    kecheng varchar(30),
    fenshu int unsigned not null
 );

 insert into fenshu (id,name,kecheng,fenshu) values(
 0,"张三","数学",75),
 (0,"李四","语文",76),
 (0,"李四","数学",90),
 (0,"王五","语文",81),
 (0,"王五","数学",100),
 (0,"王五","英语",90);

select name from fenshu group by name having min(fenshu)>80

select distinct name  from fenshu where name not in (select distinct name from fenshu where fenshu<=80);
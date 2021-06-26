drop table sawontable;

create table sawonTable (sabun number(3),
saname varchar2(10), deptno number(3) not null,
sajob varchar2(10), sapay number(10),
sahire date default sysdate,
sasex varchar2(6),
samgr number(3),
constraint sawon_sasex_ck check(sasex in('남자', '여자')),
constraint sawon_sabun_pk primary key (sabun),
constraint sawon_deptno_fk foreign key (deptno) references depttable(deptno),
constraint sawon_samgr_fk foreign key (samgr) references sawontable(sabun)
);
-- 쿼리문 (SQL문)
-- 데이터베이스에 접속하여 질의를 실행하기 위한 문법
-- 데이터베이스 벤더에 관계없이 항상 동일한 쿼리문을 사용하여
-- 데이터를 검색, 입력, 수정, 삭제할 수 있음

-- DBMS 내부에 저장된 데이터베이스의 목록을 조회하는 명령
show databases;

-- 데이터베이스에 접속하는 명령
-- USE 데이터베이스명;
use sys;
use world;
use sakila;

-- 특정 데이터베이스에 접속한 이후,
-- 해당 데이터베이스 내부에 정의된 테이블의 목록을
-- 조회하는 명령
show tables;

-- 데이터를 저장하고 있는 테이블을 조회하는 명령
-- SELECT 절 : 데이터 조회를 위한 절(명령어)
-- SELECT 컬럼명[,컬럼명] FROM 테이블명;
-- 테이블명에 작성된 테이블에서 컬럼명에 기술한 컬럼의
-- 데이터가 반환됨
select first_name
from actor;

-- select 절의 컬럼위치에 * 을 지정하면
-- 모든 컬럼을 가져옵니다.
select *
from actor;

-- 다수개의 컬럼을 지정하여 검색하는 select 절
select first_name, last_name
from actor;

-- city 테이블의 데이터를 검색하세요.
select *
from city;

-- 조건식을 사용하여 데이터를 검색하는 방법
-- WHERE 절을 추가하여 조건을 지정할 수 있음
-- city_id 컬럼의 값이 100인 데이터를 검색하는 예제
select *
from city
where city_id = 100;

select *
from city
where city_id < 50;

-- where 절을 사용하여 문자열을 비교하는 방법
-- 문자열 : ' '(" ")로 정의된 값
-- = 연산자를 사용하여 비교할 수 있음
select *
from city
where city = 'acua';

-- city 컬럼의 시작 값이 'b' 인 데이터 검색
-- 특정 문자열의 포함관계를 확인하기 위해서 사용되는 연산자
-- like 연산자
-- 컬럼명 like '검색할 문자열의 포맷'
-- % : 개수에 관계없이 모든 문자열을 의미함(없어도 관계없음)
-- _ : 한 글자를 의미함
select *
from city
where city like 'b%';

select *
from city
where city like '_b%';

-- 특정 문자열을 포함하는 데이터를 검색하는 예제
select *
from country
where country like '%south%';

-- country 테이블에서 country_id 의 값이 50 이상이면서 70 이하 인 데이터
select *
from country
where country_id >= 50 and country_id <= 70;

-- 특정 범위에 있는 값을 검색할 수 있는 between ~ and
select *
from country
where country_id between 50 and 70;

-- country_id 의 값이 11, 22, 33, 44, 55 인 데이터
-- in 연산자를 사용하여 동일 컬럼에 대한 다수개의 or 절을 간소화할 수 있음
select *
from country
where country_id in (11, 22, 33, 44, 55);

-- 데이터베이스를 생성하는 명령
-- CREATE DATABASE 데이터베이스명;
create database mydb;

-- 데이터베이스 접속
use mydb;

-- 테이블 목록 조회
show tables;

-- 테이블 생성을 위한 쿼리문
-- CREATE TABLE 테이블명 (
-- 	 컬럼명1 자료형 [제약조건]
-- 	,컬럼명2 자료형 [제약조건]
-- );
create table user_info (
	-- 기본키 설정
    -- 검색을 위해서 사용되는 컬럼을 지정
    -- 중복을 허용하지 않습니다.
	id int primary key,
    name varchar(20),
    age smallint    
);

select *
from user_info;

select count(*)
from user_info;

-- 테이블의 정보를 확인하는 명령
-- DESCRIBE 테이블명;
-- DESC 테이블명;
desc user_info;

-- 테이블 삭제 명령
-- DROP TABLE 테이블명;
drop table user_info;

-- 데이터베이스 삭제 명령
-- DROP DATABASE 데이터베이스명;
drop database mydb;

create database mydb;
use mydb;

create table user_info (
	-- 자동증가 컬럼인 경우 auto_increment 
    -- 속성을 사용할 수 있음
    -- 새로운 데이터(레코드)가 입력되면 
    -- 1부터 시작하여 1씩 증가된 값이 입력됨
	id int auto_increment primary key,
    -- 반드시 입력되어야하는 컬럼의 경우
    -- not null 제약조건을 지정할 수 있음
    name varchar(20) not null,
    age smallint
);

select *
from user_info;

-- 데이터 추가 SQL 문
-- INSERT INTO 테이블명 (데이터를 입력할 컬럼명)
-- VALUES (입력값)
insert into user_info (name, age)
values ('AAA', 10);

select *
from user_info;

insert into user_info (id, name, age)
values (3, 'BBB', 20);

select *
from user_info;

-- 전체 컬럼에 데이터를 입력하는 경우
-- 아래와 같이 테이블명만 작성해도 됩니다.
-- (컬럼명은 생략 가능)
insert into user_info 
values (7, 'CCC', 30);

select *
from user_info;

-- 특정 컬럼에 not null 제약이 존재하는 경우
-- 해당 컬럼은 반드시 데이터가 입력되어야 합니다.
insert into user_info (id, age)
values (10, 25);

-- 기본키로 지정된 컬럼은 중복된 값이 입력될 수 없습니다.
insert into user_info
values (1, 'DDD', 25);

select *
from user_info;

-- 테이블 내부의 데이터 수정을 위한 update 절
-- UPDATE 수정할테이블명
-- SET 수정할컬럼명 = 수정할값
-- WHERE 수정할 레코드를 검색하기 위한 조건식;

-- update를 실행하는 경우 아래와 같이 where 절이 생략되면
-- 모든 데이터(레코드)가 일괄적으로 수정됩니다.
update user_info
set name = '더조은';

select *
from user_info;

update user_info
set name = 'AAA'
where id = 1;

-- 테이블 내부의 데이터 삭제를 위한 DELETE 절
-- DELETE FROM 삭제할 데이터의 테이블명
-- WHERE 삭제할 레코드를 검색하기 위한 조건식

-- 트랜잭션의 정의
-- 다수개의 쿼리문을 하나의 잡으로 정의하는 역할
begin;

delete from user_info;

select *
from user_info;

-- 기존의 쿼리문의 적용 결과를 되돌림
-- (begin 이전으로 되돌림)
rollback;

commit;

delete from user_info
where id = 3;

select *
from user_info;



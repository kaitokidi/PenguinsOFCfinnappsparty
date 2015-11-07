drop table if exists entries;
create table entries (
  id integer primary key autoincrement,
  date integer not null,
  amount integer not null,
  delayed_until integer,
  reason text
);
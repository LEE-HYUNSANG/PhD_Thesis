create table if not exists ncs_unit (
  unit_code text primary key,
  unit_name text,
  unit_level int,
  unit_def text,
  large_name text, medium_name text, small_name text, detail_name text,
  version text, source_api text, last_sync_at timestamptz default now()
);

create table if not exists ncs_job_basic_skill (
  unit_code text,
  basic_name text,
  basic_factor text,
  primary key(unit_code, basic_name, basic_factor)
);

create table if not exists ncs_unit_license_map (
  unit_code text,
  unit_name text,
  jm_code text,
  jm_name text,
  total_hours int,
  basic_hours int,
  must_hours int,
  opt_hours int,
  min_hours int,
  exam_org text,
  primary key(unit_code, jm_code)
);

create table if not exists ncs_training_course (
  unit_code text,
  unit_name text,
  level int,
  train_goal text,
  train_hours int,
  facility text,
  method text,
  primary key(unit_code, train_goal, method)
);

create table if not exists ncs_academic_curriculum (
  large_cd text,
  dept text,
  subject text,
  hours int,
  credit numeric,
  theory boolean,
  practice boolean,
  teamproj boolean,
  primary key(dept, subject)
);

create table if not exists ncs_ksa_standard (
  duty_code text,
  unit_code text,
  element_no text,
  ksa_type text,
  ksa_name text,
  ksa_text text,
  primary key(duty_code, unit_code, element_no, ksa_type)
);

create table if not exists ncs_utilization (
  unit_code text,
  career_path_url text,
  career_period text,
  related_license text
);

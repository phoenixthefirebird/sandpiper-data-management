CREATE TABLE profiles(
  中文姓名 VARCHAR(64) PRIMARY KEY,
  英文姓名 VARCHAR(255),
  性别 VARCHAR(24),
  加拿大潮属社团总会职务 TEXT,
  加拿大潮属社团总会职务_英文 TEXT,
  社团职务 TEXT,
  社团职务_英文 TEXT,
  工作职务 TEXT,
  工作职务_英文 TEXT,
  联系电话 TEXT,
  联系邮箱 TEXT,
  地址 TEXT,
  政要 BOOL,
  地区 TEXT,
  关系人姓名 TEXT,
  关系 TEXT,
  更新时间 VARCHAR(255)
);

-- @block
DROP TABLE profiles;
# -*- coding: utf-8 -*-
# @Time    : 2024/11/1 16:43
# @Author  : Galleons
# @File    : resumes.py

"""
简历数据模型
"""

from pydantic import ConfigDict, BaseModel, Field, EmailStr
from typing import List, Optional
from datetime import date
from pydantic import BaseModel, EmailStr, Field, constr
from enum import Enum


class Gender(str, Enum):
    MALE = "男"
    FEMALE = "女"


class WorkType(str, Enum):
    FULL_TIME = "全职"
    PART_TIME = "兼职"
    INTERNSHIP = "实习"
    FULL_OR_PART = "全/兼职"


class DutyTime(str, Enum):
    IMMEDIATELY = "随时"
    WITHIN_WEEK = "1周内"
    WITHIN_MONTH = "1个月内"
    WITHIN_THREE_MONTHS = "3个月内"
    TO_BE_DETERMINED = "待定"


class Certificate(BaseModel):
    """证书信息"""
    certificate_name: str = Field(..., description="证书名称")
    certificate_date: Optional[date] = Field(None, description="获得日期")
    certificate_desc: Optional[str] = Field("", description="证书描述")


class WorkExperience(BaseModel):
    """工作经历"""
    company_name: str = Field(..., description="公司名称")
    position: str = Field(..., description="职位名称")
    start_date: date = Field(..., description="开始日期")
    end_date: Optional[date] = Field(None, description="结束日期")
    department: Optional[str] = Field("", description="部门")
    company_industry: Optional[str] = Field("", description="公司行业")
    company_nature: Optional[str] = Field("", description="公司性质")
    company_scale: Optional[str] = Field("", description="公司规模")
    experience_description: str = Field(..., description="工作描述")


class Education(BaseModel):
    """教育经历"""
    school_name: str = Field(..., description="学校名称")
    major: str = Field(..., description="专业")
    degree: str = Field(..., description="学历")
    start_date: date = Field(..., description="开始日期")
    end_date: date = Field(..., description="结束日期")
    major_description: Optional[str] = Field("", description="专业描述")
    gpa: Optional[str] = Field("", description="绩点")


class ProjectExperience(BaseModel):
    """项目经验"""
    project_name: str = Field(..., description="项目名称")
    company_name: Optional[str] = Field(None, description="所属公司")
    start_date: date = Field(..., description="开始日期")
    end_date: date = Field(..., description="结束日期")
    project_description: str = Field(..., description="项目描述")
    responsibility: str = Field(..., description="项目职责")


class LeadershipExperience(BaseModel):
    """领导经历"""
    position: str = Field(..., description="职位")
    start_date: date = Field(..., description="开始日期")
    end_date: date = Field(..., description="结束日期")
    experience_description: str = Field(..., description="经历描述")


class JobIntention(BaseModel):
    """求职意向"""
    industry: str = Field(..., description="期望行业")
    company_property: Optional[str] = Field(None, description="期望公司性质")
    province: str = Field(..., description="期望省份")
    city: str = Field(..., description="期望城市")
    salary_min: int = Field(..., ge=0, description="期望最低薪资")
    salary_max: int = Field(..., ge=0, description="期望最高薪资")
    job_type: WorkType = Field(..., description="工作类型")
    category: str = Field(..., description="职位类别")
    second_category: Optional[str] = Field(None, description="职位二级类别")
    parent_category: Optional[str] = Field(None, description="职位父级类别")





# 总表
class Resume(BaseModel):
    """完整的简历信息"""
    # 基本信息
    student_key: str = Field(..., description="学生唯一标识")
    name: str = Field(..., description="姓名")
    gender: Gender = Field(..., description="性别")
    id_number: constr(regex=r'^\d{17}[\dXx]$') = Field(..., description="身份证号")
    nationality: Optional[str] = Field(None, description="民族")
    birth_place: str = Field(..., description="籍贯")
    phone: constr(regex=r'^\d{11}$') = Field(..., description="手机号")
    email: EmailStr = Field(..., description="电子邮箱")
    birthday: date = Field(..., description="出生日期")
    political_status: Optional[str] = Field(None, description="政治面貌")

    # 教育和工作状态
    highest_degree: str = Field(..., description="最高学历")
    graduate_year: int = Field(..., ge=1900, le=2100, description="毕业年份")
    work_years: int = Field(0, ge=0, description="工作年限")
    current_status: Optional[str] = Field(None, description="当前状态")

    # 技能和个人描述
    skill_description: str = Field(..., description="技能描述")
    self_introduction: str = Field(..., description="自我介绍")

    # 详细信息
    education_experience: List[Education] = Field(default_factory=list, description="教育经历")
    work_experience: List[WorkExperience] = Field(default_factory=list, description="工作经历")
    project_experience: List[ProjectExperience] = Field(default_factory=list, description="项目经历")
    leadership_experience: List[LeadershipExperience] = Field(default_factory=list, description="领导经历")
    certificates: List[Certificate] = Field(default_factory=list, description="证书")
    job_intention: JobIntention = Field(..., description="求职意向")

    # 简历状态
    is_public: bool = Field(False, description="是否公开")
    language: str = Field("中文", description="简历语言")
    completion_percent: int = Field(0, ge=0, le=100, description="完成度")
    last_updated: date = Field(..., description="最后更新时间")

    class Config:
        schema_extra = {
            "example": {
                "student_key": "1cd86bcd5182f18396dc040038b66dba",
                "name": "贾馥阳",
                "gender": "女",
                "id_number": "130223199512******",
                "nationality": "汉族",
                "birth_place": "河北省",
                "phone": "16631210353",
                "email": "1003012484@qq.com",
                "birthday": "1995-12-01",
                "political_status": "共青团员",
                "highest_degree": "本科",
                "graduate_year": 2022,
                "skill_description": "CET-6、教师资格证、机动车驾驶证、普通话二级甲等；熟练使用办公软件excel、ppt、ps，会使用专业软件GIS、CAD、ERP",
                "self_introduction": "善于沟通，有良好的沟通表达能力和人际交往能力..."
            }
        }


# models.py
from typing import List, Optional
from datetime import date
from pydantic import BaseModel, EmailStr, Field, constr
from enum import Enum


# [Previous Enums and Base Models remain the same...]

class ResumeUpdate(BaseModel):
    """用于更新操作的简历模型"""
    name: Optional[str] = None
    gender: Optional[Gender] = None
    phone: Optional[constr(regex=r'^\d{11}$')] = None
    email: Optional[EmailStr] = None
    birthday: Optional[date] = None
    highest_degree: Optional[str] = None
    graduate_year: Optional[int] = Field(None, ge=1900, le=2100)
    work_years: Optional[int] = Field(None, ge=0)
    skill_description: Optional[str] = None
    self_introduction: Optional[str] = None
    education_experience: Optional[List[Education]] = None
    work_experience: Optional[List[WorkExperience]] = None
    project_experience: Optional[List[ProjectExperience]] = None
    certificates: Optional[List[Certificate]] = None
    job_intention: Optional[JobIntention] = None
    is_public: Optional[bool] = None

    class Config:
        extra = "forbid"


class ResumeResponse(Resume):
    """API响应使用的简历模型"""
    id: str = Field(..., description="简历ID")
    created_at: date = Field(..., description="创建时间")
    updated_at: date = Field(..., description="更新时间")

    class Config:
        extra = "allow"  # 允许额外字段


# 用于简历搜索的模型
class ResumeSearchParams(BaseModel):
    keyword: str = Field(..., min_length=1)
    skills: Optional[List[str]] = None
    min_experience: Optional[int] = Field(None, ge=0)
    max_salary: Optional[int] = Field(None, ge=0)


# 分页响应模型
class PaginatedResponse(BaseModel):
    total: int
    page: int
    page_size: int
    results: List[ResumeResponse]


# 错误响应模型
class ErrorResponse(BaseModel):
    detail: str
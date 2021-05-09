#!/usr/bin/evn python3
# coding=utf-8

import copy
from model.model import Setting
from dao.base import BaseDAO


class SettingDAO(BaseDAO):
    """
    对Setting表改查
    """

    @classmethod
    def update_one(cls, user_id: int, **kwargs) -> None:
        """
        # 根据用户user_id 更新Setting
        :param user_id: 主键
        :param kwargs: 更新的键值对
        """
        user = cls.db_session.query(Setting).get(user_id)
        if user:
            for key, value in kwargs.items():
                if hasattr(user, key):
                    setattr(user, key, value)

    @classmethod
    def select_setting(cls, *exclude_field) -> dict:
        """
        #查询用户setting
        :param exclude_field: 排除的字段,注意排除密码字段
        :return: dict
        """
        exclude_field = copy.deepcopy(exclude_field)
        profile = cls.db_session.query(Setting).\
            order_by(Setting.id.desc()).limit(1).one()
        # 列表生成式,排除下划线开头的字段
        field = [
            f for f in dir(profile)
            if not f.startswith("_") and f not in exclude_field
        ]
        return {key: getattr(profile, key) for key in field}



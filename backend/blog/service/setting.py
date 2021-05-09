#!/usr/bin/evn python3
# coding=utf-8

from dao.setting import SettingDAO
from service.base import BaseSrv


class SettingSrv(BaseSrv):

    @classmethod
    def get_setting(cls) -> dict:
        """
        # 获取用户配置数据
        :return: 设置字典
        """
        return SettingDAO.select_setting("metadata")

    @classmethod
    def put_setting(cls, user_id: int, data: dict) -> None:
        """
        # 更新用户配置数据
        :param user_id: 主键ID
        :param data: 更新的数据
        """
        SettingDAO.update_one(user_id, **data)



# 企业固定资产管理应用
Enterprise Fixed Asset Management Application

## 一， 项目基本情况
Enterprises generally have fixed assets, such as computers, projectors and other equipment. Industrial enterprises have many machines, instruments, and experimental equipment. The fixed assets of enterprises need to have management applications to ensure the normal use and safety of assets. Therefore, the fixed asset management application is a very common enterprise IT application. 

This project expects to obtain a simple enterprise fixed asset management application system to help enterprises manage the ownership and circulation of fixed assets. Including: asset storage, asset requisition, asset borrowing, asset transfer, asset clearing and returning, asset maintenance, asset card viewing and asset label printing, etc. Support basic approval process

## 基本功能说明 
### 主要概念
### 业务实体
业务实体 refers to a business unit that needs to manage assets independently. It can be a top-level department, it can also be a subsidairy. Assets between business entities are completely isolated and cannot be used interchangebly. 

### 资产类型
There are two types of assets
- Item Asset (条目型资产): high valued assets such as computers and projectors
- Quantitative Asset (数量型资产): low valued assets such as resistors and pens

The basic functions for this project are only managed for Item Assets first, and 数量资产 are expanded functionality 

### 资产分类 Asset Classification
Users can declare classification of assets depending on conditions. Asset classification supports multi-level structure.

### 资产实例
Asset instances are specific assets. Each instance of an itemized asset will have a unique number, such as a computer. Each instance of a quantitative asset represents a material package, which is mainly an increase or decrease in quantity in the use operation, such as an auxiliary material package.

Examples of assets include the following information: 

1) Basic information of assets. For example, asset number, name, description, brand, model, serial number, location, status, etc.

2) Ownership of assets. Including account holder, account department, and current user.

3) Financial information of assets. For example, original value, net value, depreciation mode, service life, etc.

4) Custom attributes of assets. That is, additional management attributes added by business personnel to assets, such as product line, attribution item, source purchase order number, asset usage status, etc. The life cycle state presets of asset instances include the following

- IDLE: Idle. Indicates that the asset instance currently has no user and can be used. 
- IN_USE: In use. Indicates that the asset instance has been used by the account holder. 
- IN_MAINTAIN: Under maintenance. Indicates that the asset instance is being repaired or maintained by the maintainer. - RETIRED: Retired. Indicates that the asset instance has been cleared and retired and is no longer managed. 
- DELETED: Deleted. Indicates that the asset instance data is no longer used. This state is usually used when repairing erroneous data.

### 资产操作任务
Asset operation tasks refer to task instances created by asset administrators or enterprise employees （企业资产管理员 或 企业员工）in a business process. Multiple asset instances can be associated with an operation task. For example, when an asset manager transfers multiple assets to an employee at a time, he submits a transfer operation task that contains multiple asset instances.

### 资产操作日志

The asset operation log refers to the historical log of the operation of an asset instance. For example, an asset instance has undergone operations such as creation, requisition, transfer, etc., each operation will record the operation log of the asset instance

### 主要功能

### 系统管理
1. 统一门户 Unified Portal
    - 应用门户 Application Portal (可选) ：After the employees log in to the system, the portals of different applications are displayed. For example, the asset management entry is displayed, and the interface menu after entering is the asset management application menu.
    - 菜单管理 Menu Management (可选) ：The system administrator can manage the menu items and levels of the application. Should support the configuration of a third-party URL as a menu item. Different menu items correspond to different function permissions.
2. 个人工作台
    - 待办任务 Upcoming Tasks（可选）: The entrance to the to-do tasks that employees need to handle is mainly the approval form. For example, the approval form for asset acquisition received by the supervisor
3. 系统管理
    - 登录登出 (必选)
    - 用户管理 (必选) System administrators can create users to maintain the system, reset user passwords, lock and unlock users, and set user roles
    - 角色权限 (必选) System administrators can create roles to maintain the system,
    - 导入导出管理 (可选) Asynchronous tasks need to be created when batch import or export. System administrators can view and manage asynchronous tasks, including downloading failed log files, re-executing tasks, downloading task result files, etc.
    - 操作日志 (可选) System administrators can view system operation logs, including login logs and key data modification logs


### 资产管理
1. 基础数据
    - 业务实体定义 (可选) The IT administrator creates and manages the list of business entities for the application. Business entities represent different organizations such as tenants that share the same system but are isolated from each other. The business entity can be a top-level department or a subsidiary. Assets between business entities are isolated and cannot be used with each other.
    - 资产属性定义 (可选) IT administrators define custom attributes of assets under a certain business entity for use in business customization scenarios. For example, the assets of a manufacturing company need to be designated for which production line
    - 资产分类定义 (必选) IT administrators define a hierarchical classification tree of assets. Specific assets will have to be linked to a certain level of classification. This level is classified as a natural classification of assets, that is, category.
    - 资产标签定义 (可选) The IT administrator defines a template for the content of the printed asset tag card. The printed asset label is used to stick on the asset device.
2. 组织管理
    - 组织数据管理 (必选) The asset manager views and maintains the company's organizational department data. The organization can be multi-level. The organization is used for the attribution of employees and the accounting department of assets.
    - 员工数据管理 (必选) Asset administrators view and maintain enterprise employee data. The employee and the logged-in user are associated. Employee's account holder for assets
3. 资产台账
    - 资产录入 (必选) The asset manager can enter multiple assets at once, including itemized assets and quantitative assets. There is a master-slave relationship between multiple assets, such as the host computer and monitor, and headset. The newly entered assets are first posted to an asset manager
    - 资产批量导入 (可选) Asset managers can import assets in batches through files. Scenario 1: The department newly purchased a batch of assets, which need to be quickly imported into the asset management application system; Scenario 2: The assets previously managed by manual EXCEL need to be imported into the new asset management application system.
    - 资产信息变更 (必选) The asset manager can modify the information of a single asset instance, including basic information, location, value, quantity, etc. The asset manager can change the master-slave relationship between assets. For example, associating a computer’s monitor accessory to another
    - 资产查询 (必选) Asset managers can query assets under their jurisdiction based on common conditions such as name, description, and classification. Asset administrators query assets based on asset custom attributes. The asset manager can view a full view of a single asset, including asset information, usage, maintenance history, transfer history, borrowing history, etc. The asset manager can print the label of a single asset instance for pasting on the asset device
    - 资产历史 (必选)  The asset manager or commissioner can query the history of asset changes based on common conditions, including maintenance, transfer, and borrowing.
4. 我的资产
    - 我的资产 (可选) Current employees check which assets are held under their name
5. 资产使用
    - 资产领用 (必选) Employees request assets from the asset manager. You can claim multiple assets at once. The employee first submits the application for requisition, after the supervisor’s approval and the asset manager confirms, the asset will be posted to the current employee’s name
    - 资产调拨 (可选) Asset managers allocate assets in batches to asset managers in other departments
    - 资产维保 (可选) The employee submits an application for asset repair and maintenance, and the person in charge of maintenance takes the asset for maintenance after receiving the application. After the maintenance is completed, return it to the current user.
    - 资产清退 (必选) The asset manager shall clear and return assets that have expired or are damaged or scrapped. You can clear multiple assets at once. The value of the assets that are cleared is zero and can no longer be used
    - 资产转移 (必选) An employee transfers certain assets to another employee. After the asset transfer application is submitted and approved by the supervisor, the account holder and department of the asset are switched to the new employee and department. The location of assets is also moved to a new location.
    - 资产退库 (必选) When employees' assets are no longer in use, they can submit an application for asset withdrawal. The asset manager of the current department will confirm the application after receiving the application, and the asset will be transferred back to the asset manager to be used again.
6. 资产分析
    - 资产统计 (可选) Asset managers can view the statistics of assets under their jurisdiction. Including: how many assets there are; the distribution of assets in different states; the distribution of assets in different departments; the change curve of net asset value;
    - 资产折旧 (必选) The system automatically depreciates all assets and updates the net value according to the useful life of the asset and the average life mode. For example: a computer whose original value is 10,000 yuan and its useful life is 5 years, the annual depreciation is 2,000 yuan, and the net value after 5 years is 0. After the net value is 0, you can do asset liquidation

## 预期用户 Expected Users
- 企业IT管理员: Enterprise IT Manager: configure initial data and parameters, add new functionality, maintain core data of application
- 企业系统管理员: Enterprise System Manager: manage users, roles, and logs
- 企业资产管理员: Enterprise Asset Manager: each department has its own manager who is responsible for managing the assets in warehouse and providing related services for employees
- 企业员工： all employees in the Enterprise




## 用户代数
- 联系人：苏胄
- 13142102456
- suzhou@huawei.com

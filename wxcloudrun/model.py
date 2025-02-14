from datetime import datetime

from wxcloudrun import db


# 计数表
class Counters(db.Model):
    # 设置结构体表格名称
    __tablename__ = 'Counters'

    # 设定结构体对应表格的字段
    id = db.Column(db.Integer, primary_key=True)
    count = db.Column(db.Integer, default=1)
    created_at = db.Column('createdAt', db.TIMESTAMP, nullable=False, default=datetime.now())
    updated_at = db.Column('updatedAt', db.TIMESTAMP, nullable=False, default=datetime.now())

def calculate_fold_change(target_gene, processed_gene_list, internal_reference, group, control_sample):
    for gene_name in target_gene:
        name = gene_name + '/' + internal_reference
        if name not in processed_gene_list:
            processed_gene_list.append(name)
        control_value = group.loc[group['Sample Name'] == control_sample, name].values[0]
        # 计算Fold Change
        changed_name = 'Flod Change ' + name
        if changed_name not in processed_gene_list:
            processed_gene_list.append(changed_name)
        group[changed_name] = group[name] / control_value
    return group
def allowed_file(filename):
    """检查文件扩展名是否允许"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

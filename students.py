def print_menus():
	print("="*30)
	print("输入数字1添加学生")
	print("输入数字2查找学生")
	print("输入数字3修改学生")
	print("输入数字4删除学生")
	print("输入数字5显示所有学生")
	print("输入数字6退出")

def add_student():
	name=input("请输入你要添加学生名字")
	age=input("请输入你要添加的学生年龄")
	qq=input("请输入你要添加的学生的QQ号码")
	stu={"name":name,"age":age,"qq":qq}
	stus.append(stu)
	
def search_student(name):
	for item in stus:
		if item["name"]==name:
			print("%s\t%s\t%s"%(item["name"],item["age"],item["qq"]))
			return item
	else:
		print("学生%s不存在"%name)
		
def update_student(name):
	stu=search_student(name)
	if stu!=None:
		name=input("请输入你想修改成的名字")
		age=input("请输入你想修改的日期")
		qq=input("请输入你想修改的qq号")
		stus[stus.index(stu)]={"name":name,"age":age,"qq":qq}
		print("学生%s资料修改成功"%name)
	else:
		return

def del_student(name):
	stu=search_student(name)
	if stu!=None:
		stus.remove(stu)
		print("学生%s资料删除成功"%name)
	else:
		return
		
def display_all_student():
	print("序号\t姓名\t年龄\tQQ号")
	i=1
	for stu in stus:
		print("%s\t%s\t%s\t%s"%(i,stu["name"],stu["age"],stu["qq"]))

def main():
	print_menus()
	while True:
		operation=int(input("请输入你要进行的操作"))
		if operation==1:
			add_student()
		if operation==2:
			search_student(input("请输入你要查找的学生名字"))
		if operation==3:
			update_student(input("请输入你要修改的学生名字"))
		if operation==4:
			del_student(input("请输入你要删除的学生名字"))
		if operation==5:
			display_all_student()
		if operation==6:
			break
			
stus=[]
main()	
from .company import Company
from .function import *
 
def main(q, selfurl):

    company = Company(q, selfurl)
    
    menu = {
        "add": company.add,
        "edit": company.edit,
        "remove": company.remove,
        "print": company.print,
        "clear": company.clear,
    }
    
    print("Content-type: text/html; charset=utf-8\n\n")
    load_template('header')

   	if 'type' in q:
		try:
			menu[q.getvalue('type')]()
			company.show_base()
			show_menu(q, selfurl)
		except Exception as e:
			print(e, '<br>')
	else:
		company.show_base()
		show_menu(q, selfurl)

	load_template('footer')
	company.save_base()


if __name__ == '__main__':
    main()



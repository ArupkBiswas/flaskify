from flask import Flask  #,request,render_template

app = Flask(__name__)



# @app.route('/',methods=['GET','POST'])
# def get_data():
# 	if request.method=='POST':
# 		first_name=request.form['fname']
# 		last_name=request.form['lname']
# 		emailid=request.form['emailid']
# 		connection = mysql.get_db()
# 		cursor = connection.cursor()
# 		query="INSERT INTO names_tbl(f_name,l_name,e_id) VALUES(%s,%s,%s)"
# 		cursor.execute(query,(first_name,last_name,email_id))
# 		connection.commit()
# 	return render_template("index.html")

# if __name__=='__main__':
# 	app.run(debug=True)
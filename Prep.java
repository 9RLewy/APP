package database;
import java.sql.*;
public class Prep {
	static Connection con;
	static PreparedStatement sql;
	static ResultSet res;
	
	public Connection getConnection() {
		try
		{
			Class.forName("com.mysql.cj.jdbc.Driver");// load driver
			System.out.println("registered success!");//load driver success if"registered success" printed
            // create object connection,connect database
			con =DriverManager.getConnection("jdbc:mysql://localhost:3306/?useSSL=false&serverTimezone=UTC","root","zhao1guo2chen3");
			System.out.println("connection success!");//connect database successfully if"connection success"printed
			
		}catch(Exception e) {e.printStackTrace();}
		return con;
	}

	public static void main(String[] args) {
		Prep c = new Prep();
		con = c.getConnection();
		try
		{
			sql = con.prepareStatement("select*from users_database.students_info");
			res= sql.executeQuery();
			System.out.println("--------------");
			System.out.println("The information of student users in the database:");
			System.out.println("--------------");
			System.out.println("|ID           |name       |Age  |");
			// check all the data in the database
			while(res.next()) {
				String id = res.getString("ID");
				String name =  res.getString("Name");
				String age = res.getString("Age");
				System.out.print("|  "+id+"   |");
				System.out.print(name+"        |");
				System.out.println(age+"   |");
				
			}
			//add a data
			/*
			sql =con.prepareStatement("insert into users_database.students_info "+"values(?,?,?)");
            sql.setInt(1, 20170004);
            sql.setString(2, "Lewy");
            sql.setString(3, "22");
            System.out.println("--------------");
			sql.executeUpdate();*/
			
			//change a data's information
			sql =con.prepareStatement("update users_database.students_info set Age "+"= ? where ID = 2017001");
			sql.setString(1,"19");
			sql.executeUpdate();
			/*//delete a data in database
			sql =con.prepareStatement("delete from users_database.students_info where ID = 20170005");
			sql.executeUpdate();*/
			res.close();
			con.close();

		}
		catch(SQLException e)
		{
			System.err.println("SQLException: " + e.getMessage());
		}
		finally{
		}


}
}

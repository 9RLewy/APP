package main1;

import java.sql.*;

public class connect {
	static Statement sql1;
    static PreparedStatement sql;
    static ResultSet res;
	public static void main(String[] args) {
		Connection conn=null;
		try
		{
			Class.forName("com.mysql.cj.jdbc.Driver");// �����������򣬴˴��������
			System.out.println("registered success!");//���registered success��ʾ�������سɹ�
			//�����������ӣ��������ݿ⣬������employeedbmsΪ���ݿ�����rootΪ�û�����123456λ���룬������������ʵ����������޸ģ�������������䶯��ע��ȷ�����ݿ������û����������׼ȷ�ԡ�
			conn =DriverManager.getConnection("jdbc:mysql://localhost:3306/?useSSL=false&serverTimezone=UTC","root","zhao1guo2chen3");
			System.out.println("connection success!");//���connection success��ʾ���ݿ��ѳɹ�����
			sql1 = conn.createStatement();
			res= sql1.executeQuery("select*from users_database.students_info");
			System.out.println("--------------");
			System.out.println("The information of student users in the database:");
			System.out.println("--------------");
			System.out.println("|ID    |name       |password |");
			// check all the data in the database
			while(res.next()) {
				String id = res.getString("ID");
				String name =  res.getString("Name");
				String password = res.getString("Password");
				System.out.print("|  "+id+"   |");
				System.out.print(name+"    |");
				System.out.println(password+" |");
				
			}res.close();
			//add a data
			sql =conn.prepareStatement("insert into users_database.students_info "+"values(?,?,?)");
            sql.setInt(1, 3);
            sql.setString(2, "liyanxin");
            sql.setString(3, "123456");
            System.out.println("--------------");
			sql.executeUpdate();
			/*
			//change a data's information
			sql =conn.prepareStatement("update users_database.students_info set password "+"= ? where ID=3");
			sql.setString(1,"457");
			sql.executeUpdate();
			//delete a data in database
			sql =conn.prepareStatement("delete from users_database.students_info where id = 3");
			sql.executeUpdate();*/
			conn.close();
		}
		catch(Exception e)
		{
			System.out.println("error!");
		}
		finally{
		}
		// TODO �Զ����ɵķ������

	}

}

import java.util.*;


class LastSession{

    String start_time;
    int slot_alloted;

    LastSession(){}

    LastSession(String start_time,int slot){

         this.start_time  =start_time;
         this.slot_alloted=slot_alloted;

    }

}

class transaction{

	double fee_paid;
	String start_time,end_time;

	transaction(){}

	transaction(double fee_paid,String start_time,String end_time){

         this.fee_paid  =fee_paid;
         this.start_time=start_time;
         this.end_time  =end_time;

	}


}


class user{

	String userID, name, phno;
	double balance;
    LastSession session=null;
    ArrayList<transaction> trans = new ArrayList<>();

    user(){}

    user(String userID, String name , String phno ,double balance ){

    	this.userID =userID;
    	this.phno   =phno;
    	this.name   =name;
    	this.balance=balance;

    }

}
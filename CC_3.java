public class second {
    public static void sendMail(String address, String subject, String body) {
        Messaging.SingleEmailMessage mail = new Messaging.SingleEmailMessage();
        String[] toAddresses = new String[]{address};  
        mail.setToAddresses(toAddresses);
        mail.setSubject(subject);
        mail.setPlainTextBody(body);
        Messaging.sendEmail(new Messaging.SingleEmailMessage[]{mail});  
    }
}

	
	
	//Apex code
	String Addresses='recipients-addresses';
	String subject='LP-2 assignment confirmation';
	String body='Cloud Computing Assignment 3 implemented succssfully';
	second.sendMail(Addresses,subject,body);
	
		 
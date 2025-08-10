select
 round(
    sum(case 
        when order_date= customer_pref_delivery_date  then 1 else 0 end
        )*1.0/count(customer_id)*100
    ,2) 
as immediate_percentage  
from (select d.customer_id,order_date,customer_pref_delivery_date from delivery d where order_date<=(select min(order_date) from delivery where customer_id=d.customer_id ) group by customer_id  ) s
 
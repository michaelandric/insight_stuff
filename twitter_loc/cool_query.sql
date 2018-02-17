SELECT subtable.rt_influence*subtable.fav_influence AS influence FROM
	(SELECT rt_count, user_followers_count, rt_count/user_followers_count::float AS rt_influence, 
	fav_count, fav_count/user_followers_count::float AS fav_influence 
	FROM la_tweets WHERE rt_count > 0 AND fav_count > 0 AND user_followers_count > 0 
	ORDER BY rt_influence DESC) AS subtable ORDER BY influence DESC LIMIT 20;

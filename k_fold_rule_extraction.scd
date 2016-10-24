//..........................................................
//	This file opens the X_train_k.csv and y_train_k.csv    .
//  files and apply rule-extraction to each set            .
//..........................................................

(
"/home/ivan/documents/in-construction/rule_extraction_function.scd".load;
"/home/ivan/documents/in-construction/scaling_rules.scd".load
);
(
~intervals_and_distances = [
	[
		[ [0, inf], 1000 ]
		//[ [0, 15], 5], [ [15,55], 10], [ [55,inf], 500]
	],
	[
		[ [0,inf], 1000 ]
	]
]);

(
for(0,9,{
	arg i;
x = CSVFileReader.readInterpret("/home/ivan/documents/in-construction/X_train_"++i.asString++".csv");
y = CSVFileReader.readInterpret("/home/ivan/documents/in-construction/y_train_"++i.asString++".csv");
//data
~data = [];
x.do{arg x, i;
	x = x.add(y[i][0]);
	~data = ~data.add(x)
};
~rules = ~subsetsCompression.value(~data,~intervals_and_distances);
~bag = ~bagOfRules_uncompleted.value(~rules);
~scaled_rules = ~scaling_Rules.value(~bag,~data);

//  Export first and second parameters + class
(
f = File("/home/ivan/documents/in-construction/p_a_r_1_"++i.asString++".csv", "w");
~scaled_rules.do{ arg x;
	if(x[0].size==0){
		f.write(x[0]+","+x.last+"\n")}{
			x[0].do{arg y;
				f.write(y+",")
			};
			f.write(x.last+"\n");
		}
	};
	f.close
);
(
f=File("/home/ivan/documents/in-construction/p_a_r_2_"++i.asString++".csv","w");
~scaled_rules.do{ arg x;
	if(x[1].size==0){f.write(x[1]+","+x.last+"\n")}{
		x[1].do{ arg y; f.write(y + ",")};
		f.write(x.last+"\n")
	}
};
f.close
)


})
);

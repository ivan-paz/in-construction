//  Find min max for each feature
(
~min_max = {arg data;
	var max, min, size, column, difference, range = [];
	if(data.size > 1){
		size = (0 .. data[0].size - 2);
		size.do{|col|
			column = data.slice(nil, col);
			//column.postln;
			min = column.minItem;
			max = column.maxItem;
			range = range.add([min,max]);
		}};
		range
	}
);
//~min_and_max_values = ~min_max.value(~data)
//    Rescaling features values into interval [0,1]
(~scaling = { arg x, feature, min_and_max_values;
	var scaled, minx, maxx;
	minx = min(min_and_max_values[feature][0],min_and_max_values[feature][1]);
	maxx = max(min_and_max_values[feature][0],min_and_max_values[feature][1]);
	scaled = (x - minx) / (maxx - minx)
});
//~scaling.value(1, 1, ~min_and_max_values);

(~scaling_Rules = { arg rules, data;
	var min_and_max_values;
	var scaled_rules = [];
	min_and_max_values = ~min_max.value(data);
	min_and_max_values;
	rules.do{arg rule;
		var temporal_rule = [];
		//instance.postln;
		(rule.size -1).do{arg i;
			var scaled_value;
			var value;
			var interval = [];
			value = rule[i];
			//'i : '.post; i.postln;
			//'value  '.post; value.postln;
			if(value.size==0){
			scaled_value = ~scaling.value(value,i,min_and_max_values);
			temporal_rule = temporal_rule.add(scaled_value)}{
				value.do{
					arg value2;
					var scaled_value2;
					scaled_value2 = ~scaling.value(value2,i,min_and_max_values);
					interval = interval.add(scaled_value2);
				};
				temporal_rule = temporal_rule.add(interval);
			};
		};
		temporal_rule = temporal_rule.add(rule.last);
		scaled_rules = scaled_rules.add(temporal_rule);
	};
	scaled_rules
})

//(~rules = [
//	[1, [1,2,3],2],
//	[[1,2,3],1,1]
//];
//~data = [
//	[1,1,1],
//	[2,2,2],
//	[3,3,1]
//]
//)
//~scaling_Rules.value(~rules, ~data);

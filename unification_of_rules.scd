//&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
//
//                    script for
//              unification of rules
//
//&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

//(//  data set for proves
//(~rules = [
//	[3,   [33, 659], 1],
//	[100, [33, 659], 1],
//	[3,   [21, 33],  1],
//	[3,   300,       1]
//]);
//~intervals_and_distances = [
  //    [
//
  //            [ [0, inf], 1000]//,  [ [1, inf],  44 ]
//
  //    ],
//
  //    [
//
  //            [ [0,inf], 500 ]
    //  ]
//]
//)
//&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
(~unification_of_rules = {
arg rules, intervals_and_distances;
var indexes; var result = [];
var newIntervals, deleteIndexes;
var temporalRules = rules.deepCopy;///////
indexes = (0 .. rules[0].size - 2);
indexes.collect{ arg colToExclude;
	//var temporalRules = rules;
	var section, subsets, selection;
	var temporal = [];
	section = (0.. indexes.size).removing(colToExclude);
	subsets = temporalRules.slice(nil,section);
	selection = temporalRules.slice(nil,colToExclude);
	subsets.do{ arg row, i;
		var values = [], indexes = [];
		//'row : '.post; row.postln;
		values = values.add(selection[i]);indexes=indexes.add(i);
		subsets.do{ arg row1, j;
		if((row==row1) && (i!=j)){
			if(row1.notNil){
			values = values.add(selection[j]);
			indexes = indexes.add(j)};
		}};
		if(values.size>1){ //values.post; indexes.postln;
		newIntervals = ~unify_intervals.value(values,indexes,colToExclude,intervals_and_distances)[0];
		deleteIndexes = ~unify_intervals.value(values,indexes,colToExclude,intervals_and_distances)[1];
		//[newIntervals,deleteIndexes].postln;
		//////////   update
		newIntervals.collect{ arg interval;
			var newRule;
			newRule = temporalRules[i];
			if(newRule.notNil){newRule[colToExclude]=interval;
			temporalRules = temporalRules.add(newRule)}};
			deleteIndexes.collect{arg index;
				temporalRules[index]=nil
		}
	};
};
//'&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&'.postln;
};
temporalRules.do{arg x;
	if(x.notNil){result = result.add(x)}};
result
});
//~unification_of_rules.value(~rules,~intervals_and_distances);
(~find_threshold ={arg value, colToExclude, intervals_and_distances;
	var threshold;
	intervals_and_distances[colToExclude].do{ arg interval;
		if((value>interval[0][0])&&(value<=interval[0][1])){threshold=interval[1]}
	};
	threshold;
});
//~find_threshold.value(3,0,~intervals_and_distances);
//&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
//             function than receives the values and
//          creates new intervals considering thresholds
//&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
(~unify_intervals = {
	arg values,indexes,colToExclude,intervals_and_distances;
	var unifiedIntervals = [];
	var indexesOfunifiedIntervals = [];
	var threshold;
	var passing = [];
	var flag = 0;
	var flatArray, newInterval;
	(values.size-1).do{arg i;
		if(flag==0){passing = passing.add(values.first)}{
			passing = passing.add([flatArray[0],flatArray[3]])};
		values = values[1..];
		//passing.postln;
		//values.postln;
		a = ~class.value(passing.last);
		b = ~class.value(values.first);
		flatArray = [a,b].flat.sort;
		threshold = ~find_threshold.value(flatArray[1],colToExclude,intervals_and_distances);
		if(
			(abs(flatArray[0]-flatArray[1])<threshold) &&
			(abs(flatArray[1]-flatArray[2])<threshold) &&
			(abs(flatArray[2]-flatArray[3])<threshold)
	){
		//'true'.postln;
		if(unifiedIntervals.indexOfEqual([flatArray[0],flatArray[3]]).isNil){ if(flatArray[0]!=flatArray[3]){
		unifiedIntervals = unifiedIntervals.add([flatArray[0],flatArray[3]])}};
		flag = 1;
		if(indexesOfunifiedIntervals.indexOfEqual(indexes[i]).isNil){
		indexesOfunifiedIntervals = indexesOfunifiedIntervals.add(indexes[i])};
		if(indexesOfunifiedIntervals.indexOfEqual(indexes[i+1]).isNil){
		indexesOfunifiedIntervals = indexesOfunifiedIntervals.add(indexes[i+1])};
}{flag=0};
	};
	[unifiedIntervals,indexesOfunifiedIntervals]
});
//~unify_intervals.value([[33,659],[21,33],300],[0,2,3],0,~intervals_and_distances)
(~class = {arg x;
	var a, b;
	if(x.class!=Array){a=x;b=x}{a=x[0];b=x[1]};
	[a,b]
});
//~class.value(2)

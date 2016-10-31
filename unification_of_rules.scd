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
//
(~rules = [
	[8, [16,48], 1],
	[8, [48, 783], 1]
];
~intervals_and_distances = [
    [
		[ [0, inf], 1000]//,  [ [1, inf],  44 ]

	],
	[
		[ [0,inf], 500 ]
	]
])
//-------------------------------------------------------------------
(~unification_of_rules = {
arg rules, intervals_and_distances;
var indexes; var result = [];
var intAndIndex;
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
		if(values.size>1){'$$$$'.postln; values.post; indexes.postln;
			intAndIndex=~unify_intervals.value(values,indexes,colToExclude,intervals_and_distances).postln;

		}
}
};
//temporalRules.do{arg x;
//	if(x.notNil){result = result.add(x)}};
//result
});
~unification_of_rules.value(~rules,~intervals_and_distances);


//-------------------------------------------------------------------
(~find_threshold ={arg value, colToExclude, intervals_and_distances;
	var threshold;
	intervals_and_distances[colToExclude].do{ arg interval;
		if((value>interval[0][0])&&(value<=interval[0][1])){threshold=interval[1]}
	};
	threshold;
});
//~find_threshold.value( 48, 0, ~intervals_and_distances);

//&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
//             function than receives the values and
//          indexes and unify the intervals considering thresholds
//&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
(~unify_intervals = {|values,indexes,colToExclude,intervals_and_distances|
	var interval, extension;
	var threshold, currentInterval=[nil,nil];
	var flag = 0;
	var temp;
	var result = [];
	var tempIndex = [];
	var deleteIndexes = [];
	(values.size - 1).do{ |i| //'i : '.post; i.postln;
		if(flag==0){interval = ~limits.value(values[i])}{
		interval=currentInterval};
		extension = ~limits.value(values[i+1]);
		threshold = ~find_threshold.value(interval[1],colToExclude,intervals_and_distances);

		//'comparando : '.post;[ interval[1],extension[0] ].postln;

		if( abs(interval[1]-extension[0])<= threshold ){
			flag=1;
			currentInterval[0]=min(interval[0],extension[0]);
			currentInterval[1]=max(interval[1],extension[1]);
			tempIndex = tempIndex.add(i);
			tempIndex = tempIndex.add(i+1);
		}{
			flag = 0;
			temp = currentInterval.deepCopy;
			//'Temp : '.post; temp.postln;
			result = result.add(temp);
			//'result ==== '.post; result.postln;
			deleteIndexes = deleteIndexes.add([tempIndex.first,tempIndex.last]);
			tempIndex = [];
		}
	};
	if(flag==1){result = result.add(currentInterval);deleteIndexes = deleteIndexes.add(tempIndex)};
	[result,deleteIndexes]
});
//~unify_intervals.value([[48,783],[16,48]],[1,0],0,~intervals_and_distances)
//~unify_intervals.value([ [16,48], [48,783],[10,48],1880,2000,5000, 5020] , [0,1,2,3,4,5,6],0,~intervals_and_distances )

//-------------------------------------------------------------------
(~limits ={|value| var left, right;
	if(value.class!=Array){left=value;right=value}{
	left=value[0];right=value[1]};
	[left,right]});
//-------------------------------------------------------------------
(~compare = {|interval,extension|
	var one, two, three, four;
	var all = [];
	interval.collect({|x| all = all.add(x)});
	extension.collect({|x| all = all.add(x)});
	one = all.minItem;
	four = all.maxItem;
	all = all.removeAt(one); 
	all;
});
~compare.value([1,2],[4,3])

a = [1,2,3,4,5]
a.removeAt(2)

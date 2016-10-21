//&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
//                    script for
//              unification of rules
//
//&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
(
//  data set for proves
(~rules = [
	[3,   [33, 659], 1],
	[100, [33, 659], 1],
	[3,   [21, 33],  1],
	[2,   300,       1]
]);
~intervals_and_distances = [
      [

              [ [0, inf], 1000]//,  [ [1, inf],  44 ]

      ],

      [

              [ [0,inf], 1000 ]
      ]
]
)
//&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
(~unification_of_rules = {
arg rules, intervals_and_distances;
var indexes;
indexes = (0 .. rules[0].size - 2);
indexes.collect{ arg colToExclude;
	var temporalRules = rules.deepCopy;
	var section, subsets, selection;
	section = (0.. indexes.size).removing(colToExclude);
	subsets = temporalRules.slice(nil,section);
	selection = temporalRules.slice(nil,colToExclude);
	subsets.do{arg row,i;
		'row: '.post; row.postln;
		subsets.do{arg row1,j;
			var values = [];
		if((row==row1)&&(i!=j)){
			values = values.add(selection[i]);
			values = values.add(selection[j]);
			'row1: '.post;row1.postln;
		};
		if(values.size>1){
		values.postln;
		//   unify intervals( values )

		}
		}
	}
}
});
~unification_of_rules.value(~rules,~intervals_and_distances);

(~find_threshold ={arg value, position, intervals_and_distances;
	var threshold;
	intervals_and_distances[position].do{ arg interval;
		if((value>interval[0][0])&&(value<interval[0][1])){threshold=interval[1]}
	};
	threshold;
});
~find_threshold.value(3,0,~intervals_and_distances);


(~unify_intervals = {arg values;
	values.size-1.do{arg i;
		var threshold;
		var newInt;
		values[i].postln;
		values[i+1].postln;
		threshold = ~find_threshold.value(values[i][0],0,~intervals_and_distances);
		if(abs(values[i][0]-values[i+1][0])<threshold){
		newInt = [min(values[i][0],values[i+1][0]),max(values[i][1],values[i+1][1])];
		'newInt: '.post; newInt.postln;
		values[i]=nil;
		values[i+1]=newInt;
		}
	};
	values
})
(
var values = [[21, 33], [33, 659]];
~unify_intervals.value(values).postln
)

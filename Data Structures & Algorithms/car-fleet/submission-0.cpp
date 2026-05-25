class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        // Idea: somehow compare the relative position of cars.
        // see how long or how manu hours will eacg car take to reach target
        // based on that stack up the min speed between 2 cars that reach a target first. t
        // then keep moving and see if another car coincides with position, 
        // if yes, stack the min speed out of those. 
        // IDK i dont know the logic here, 
        // 1 make a relative position vs time list of cars. 
        // 2 compare the time, 
        // if a lower position car takes less time than higher position car, keep the car in fleet. 
        // if it takes more time, add it to fleet . i.e it gets added to fleet. 

        int n = position.size();
        vector<pair<int, double>> cars;

        for(int i = 0; i<n; i++){
            double time = (double)(target - position[i])/speed[i];
            cars.push_back({position[i], time});

        }
        sort(cars.rbegin(), cars.rend());
        stack<double> st;
        for(auto& [pos, time]:cars){
            if(st.empty() || time>st.top()){
                st.push(time);
            }

        }
        return st.size();



        
    }
};
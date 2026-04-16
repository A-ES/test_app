import React, { useState } from 'react';
import './App.css'; // Assume basic CSS exists

export default function App() {
  const [count, setCount] = useState(0);
  const [todos, setTodos] = useState(['Learn React', 'Test Vector++']);
  const [inputValue, setInputValue] = useState('');

  // BUG 1: Counter increments by 2 instead of 1
  const handleIncrement = () => {
    setCount(prevCount => prevCount + 1); 
  };

  const handleAddTodo = () => {
    if (inputValue.trim() !== '') {
      setTodos([...todos, inputValue]);
      setInputValue('');
    }
  };

  // BUG 3: Setting to undefined instead of empty array causes a crash on render
  const handleClearTodos = () => {
    setTodos([]); 
  };

  return (
    <div className="App" style={{ padding: '20px', fontFamily: 'sans-serif' }}>
      <h1>Vector++ Test App</h1>
      
      {/* Counter Section */}
      <section style={{ marginBottom: '30px', padding: '10px', border: '1px solid #ccc' }}>
        <h2>Counter</h2>
        <p>Current Count: {count}</p>
        <button onClick={handleIncrement}>Increment</button>
      </section>

      {/* Todo Section */}
      <section style={{ padding: '10px', border: '1px solid #ccc' }}>
        <h2>Todo List</h2>
        
        <div style={{ marginBottom: '10px' }}>
          <input 
            type="text" 
            value={inputValue} 
            onChange={(e) => setInputValue(e.target.value)} 
            placeholder="New todo item..."
          />
          {/* BUG 2: Weird logic that disables button if length is exactly 5 */}
          <button 
            onClick={handleAddTodo}
            disabled={inputValue.length === 5}
          >
            Add Todo
          </button>
        </div>

        <ul>
          {/* If todos is undefined (due to Bug 3), this will throw a TypeError */}
          {todos.map((todo, index) => (
            <li key={index}>{todo}</li>
          ))}
        </ul>

        <button onClick={handleClearTodos} style={{ marginTop: '10px', color: 'red' }}>
          Clear All Todos
        </button>
      </section>
    </div>
  );
}

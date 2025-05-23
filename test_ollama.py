#!/usr/bin/env python3
"""
Simple test script to verify Ollama integration with Pokemon Gym
"""

import os
import sys
from openai import OpenAI

def test_ollama_connection():
    """Test if Ollama is running and accessible"""
    try:
        # Get Ollama base URL from environment or use default
        ollama_base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434/v1")
        
        # Create OpenAI client pointing to Ollama
        client = OpenAI(
            api_key="ollama",  # Ollama doesn't require a real API key
            base_url=ollama_base_url
        )
        
        # Test with a simple completion
        response = client.chat.completions.create(
            model="gemma3:4b",  # Use available vision model
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Say hello and confirm you can see this message."}
            ],
            max_tokens=50,
            temperature=0.7
        )
        
        print("✅ Ollama connection successful!")
        print(f"Response: {response.choices[0].message.content}")
        return True
        
    except Exception as e:
        print(f"❌ Ollama connection failed: {e}")
        print("\nTroubleshooting:")
        print("1. Make sure Ollama is installed and running")
        print("2. Pull a vision model: ollama pull gemma3:4b")
        print("3. Check if Ollama is running on the correct port")
        print(f"4. Current base URL: {ollama_base_url}")
        return False

def test_pokemon_agent_import():
    """Test if the Pokemon agent can be imported with Ollama provider"""
    try:
        sys.path.append('agents')
        from demo_agent import AIServerAgent
        
        # Try to create an agent with Ollama provider
        agent = AIServerAgent(
            provider="ollama",
            model_name="gemma3:4b"
        )
        
        print("✅ Pokemon agent with Ollama provider created successfully!")
        return True
        
    except Exception as e:
        print(f"❌ Failed to create Pokemon agent with Ollama: {e}")
        return False

if __name__ == "__main__":
    print("Testing Ollama integration with Pokemon Gym...\n")
    
    # Test 1: Ollama connection
    print("Test 1: Ollama Connection")
    ollama_ok = test_ollama_connection()
    print()
    
    # Test 2: Pokemon agent import
    print("Test 2: Pokemon Agent Import")
    agent_ok = test_pokemon_agent_import()
    print()
    
    # Summary
    if ollama_ok and agent_ok:
        print("🎉 All tests passed! Ollama integration is working.")
        print("\nYou can now run:")
        print("python agents/demo_agent.py --provider ollama --model gemma3:4b")
    else:
        print("⚠️  Some tests failed. Please check the issues above.")
        sys.exit(1) 
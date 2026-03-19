

# also

Calls the specified function block with this value as its argument and returns this value.

```kotlin
@IgnorableReturnValueinline fun <T> T.also(block: (T) -> Unit): T(source)
```

```kotlin
val greeting = "Hello".also { println("Original value: $it") }
    .uppercase()
    .also { println("Modified value: $it") }

println("Final result: $greeting")  // Outputs: FINAL RESULT: HELLO
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/also.html)

    
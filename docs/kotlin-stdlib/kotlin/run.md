

# run

Calls the specified function block and returns its result.

```kotlin
@IgnorableReturnValueinline fun <R> run(block: () -> R): R(source)
```

```kotlin
val result = run {
    val a = 5
    val b = 7
    a * b
}
println("Result: $result")
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/run.html)

    
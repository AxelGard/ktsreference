

# repeat

Executes the given function action specified number of times.

```kotlin
inline fun repeat(times: Int, action: (Int) -> Unit)(source)
```

```kotlin
fun main() {
    // Print numbers 0 to 4
    repeat(5) { index ->
        println("Current index: $index")
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/repeat.html)

    
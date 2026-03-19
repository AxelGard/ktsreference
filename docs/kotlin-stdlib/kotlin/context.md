

# context

Runs the specified block with the given value in context scope.

```kotlin
inline fun <T, R> context(with: T, block: context(T) () -> R): R(source)
```

```kotlin
fun main() {
    val doubled = context(5) {
        this * 2
    }
    println(doubled)  // Prints: 10
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/context.html)

    
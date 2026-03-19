

# foldRight

Accumulates value starting with initial value and applying operation from right to left to each element and current accumulator value.

```kotlin
inline fun <T, R> Array<out T>.foldRight(initial: R, operation: (T, acc: R) -> R): R(source)
```

```kotlin
val arr = arrayOf("a", "b", "c")
val result = arr.foldRight("") { value, acc -> value + acc }
println(result) // prints "cba"
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/fold-right.html)

    
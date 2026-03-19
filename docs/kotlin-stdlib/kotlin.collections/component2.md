

# component2

Returns 2nd element from the array.

```kotlin
inline operator fun <T> Array<out T>.component2(): T(source)
```

```kotlin
val numbers = arrayOf(10, 20, 30)

val secondElement: Int = numbers.component2()

println("The second element is $secondElement")  // Output: The second element is 20
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/component2.html)

    
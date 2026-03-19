

# contains

Returns true if element is found in the array.

```kotlin
operator fun <T> Array<out T>.contains(element: T): Boolean(source)
```

```kotlin
val fruits = arrayOf("apple", "banana", "cherry")

val hasBanana = "banana" in fruits   // true
val hasMango = "mango" in fruits     // false

println("Contains banana? $hasBanana")   // Contains banana? true
println("Contains mango? $hasMango")     // Contains mango? false
```


[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/contains.html)

    
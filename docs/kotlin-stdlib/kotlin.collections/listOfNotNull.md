

# listOfNotNull

Returns a new read-only list either of single given element, if it is not null, or empty list if the element is null. The returned list is serializable (JVM).

```kotlin
fun <T : Any> listOfNotNull(element: T?): List<T>(source)(source)
```

```kotlin
val listWithElement = listOfNotNull("Kotlin")   // [Kotlin]
val emptyList        = listOfNotNull<String>(null)   // []

println(listWithElement)   // [Kotlin]
println(emptyList)         // []
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/list-of-not-null.html)

    